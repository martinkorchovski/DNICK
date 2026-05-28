from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Pregled, Pacient


@receiver(pre_save, sender=Pregled)
def pregled_status_adjustment(sender, instance, **kwargs):
    # Ako pregldot e zavrsen a terminot e vo idnina, smeni vo zakazan
    if instance.status == 'zavrsen' and instance.termin > now():
        instance.status = 'zakazan'

    # Ako pregldot e zakazan a terminot e vo minatoto, smeni vo zavrsen
    if instance.status == 'zakazan' and instance.termin < now():
        instance.status = 'zavrsen'

    # Bonus: ako lekarot ima 3+ razlicni pacienti od ista institucija
    if instance.pk is None and instance.patient_id is not None:
        lekar = instance.glaven_lekar
        institucija = instance.patient.institucija
        pacient_ids = (
            Pregled.objects
            .filter(
                glaven_lekar=lekar,
                patient__institucija=institucija,
            )
            .values_list('patient_id', flat=True)
            .distinct()
        )
        if len(pacient_ids) >= 3:
            instance.zabeleska = (
                f"High workload with patients from institution "
                f"{institucija}."
            )


@receiver(pre_delete, sender=Pacient)
def cleanup_pregledi(sender, instance, **kwargs):
    for pregled in Pregled.objects.filter(patient=instance):
        if pregled.status == 'zakazan':
            pregled.delete()
        elif pregled.status == 'vo_tek':
            pregled.zabeleska = (
                "Patient record missing - appointment preserved for "
                "audit purposes."
            )
            pregled.save()
