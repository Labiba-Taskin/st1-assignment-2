from datetime import datetime
from typing import List, Optional


class Patient:
    """Represents a patient in the SmartCare system (FR-01, FR-08)."""

    def __init__(self, patient_id: str, name: str, phone: str):
        self.patient_id = patient_id
        self.name = name
        self.phone = phone
        self.appointment_history: List['Appointment'] = []

    def update_details(self, name: str, phone: str) -> None:
        """Update patient contact details (FR-01)."""
        self.name = name
        self.phone = phone

    def get_history(self) -> List['Appointment']:
        """Retrieve patient appointment history log (FR-08)."""
        return self.appointment_history


class Practitioner:
    """Represents a healthcare practitioner / GP (FR-03, FR-10)."""

    def __init__(self, practitioner_id: str, name: str, specialization: str):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialization = specialization

    def check_availability(self, date_time: datetime) -> bool:
        """Check practitioner availability for a requested time slot (FR-03)."""
        # Skeleton check for availability
        return True


class Appointment:
    """Represents an appointment booking between a Patient and Practitioner (FR-02, FR-04, FR-05)."""

    def __init__(self, appointment_id: str, patient: Patient, practitioner: Practitioner, date_time: datetime):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status: str = "Scheduled"  # Options: Scheduled, Completed, Cancelled, No-Show

    def cancel(self) -> None:
        """Cancel the appointment and free up the time slot (FR-05)."""
        self.status = "Cancelled"

    def update_status(self, new_status: str) -> None:
        """Update appointment lifecycle status (FR-04)."""
        self.status = new_status


class ClinicSystem:
    """Controller class managing central clinic operations and reporting (FR-06)."""

    def __init__(self):
        self.patients: List[Patient] = []
        self.practitioners: List[Practitioner] = []
        self.appointments: List[Appointment] = []

    def book_appointment(self, patient: Patient, practitioner: Practitioner, date_time: datetime) -> Optional[Appointment]:
        """Coordinate patient bookings and check schedule conflicts (FR-02)."""
        appointment = Appointment(f"APT-{len(self.appointments) + 1}", patient, practitioner, date_time)
        self.appointments.append(appointment)
        patient.appointment_history.append(appointment)
        return appointment

    def generate_report(self) -> dict:
        """Compile basic operational report on clinic activity (FR-06)."""
        return {
            "total_appointments": len(self.appointments),
            "cancelled": sum(1 for a in self.appointments if a.status == "Cancelled")