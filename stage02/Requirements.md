## 1. Problem and Scope
* **Problem Statement:** SmartCare Clinic manages appointments using fragmented paper and spreadsheet systems[cite: 2, 3]. This leads to duplicate bookings, lost records, inconsistent status tracking, missing availability, manual cancellations, and lack of reporting[cite: 2, 3].
* **In Scope:** A simple, maintainable software prototype to manage patients, practitioners, and appointment bookings/cancellations[cite: 2, 3].
* **Out of Scope (Provisional):** Full hospital management, billing, online payments, lab result tracking, and automated SMS notifications[cite: 2, 3].


## 2. Stakeholders
| Stakeholder | Need | Evidence |
| :--- | :--- | :--- |
| **Clinic Receptionist** | Quick patient lookup and real-time appointment booking without duplicates[cite: 1, 2] | Case study states clinic suffers duplicate bookings and manual cancellation friction[cite: 2]. |
| **Healthcare Practitioner (GP)** | Clear daily schedule and reliable patient appointment history[cite: 1, 2] | Case study highlights limited visibility of availability and lack of history[cite: 2]. |
| **Clinic Management** | Operational reports on booking volumes and appointment statuses[cite: 1, 2] | Case study explicitly notes difficulty producing basic operational reports[cite: 2]. |
| **Patient** | Reliable appointment scheduling and clear status tracking[cite: 1, 2] | Case study notes inconsistent appointment status and manual processes[cite: 2]. |


## 3. Functional Requirements
* **FR-01:** The system shall allow receptionists to register and update patient profile records[cite: 1, 2].
* **FR-02:** The system shall enable receptionists to search patient records by name, phone number, or ID[cite: 1, 2].
* **FR-03:** The system shall allow receptionists to view real-time daily schedules for all GPs[cite: 1, 2].
* **FR-04:** The system shall prevent duplicate bookings for the same practitioner in the same time slot[cite: 1, 2].
* **FR-05:** The system shall record appointment bookings with patient, practitioner, date, and time details[cite: 1, 2].
* **FR-06:** The system shall allow receptionists to update appointment status (Scheduled, Completed, Cancelled, No-Show)[cite: 1, 2].
* **FR-07:** The system shall free up the practitioner's time slot immediately upon appointment cancellation[cite: 1, 2].
* **FR-08:** The system shall maintain an immutable history of past appointments for each patient[cite: 1, 2].
* **FR-09:** The system shall allow receptionists to re-schedule existing appointments to new time slots[cite: 1, 2].
* **FR-10:** The system shall generate operational summary reports on total bookings, cancellations, and status breakdowns[cite: 1, 2].
* **FR-11:** The system shall display practitioner availability filtered by specific dates or time windows[cite: 1, 2].
* **FR-12:** The system shall validate patient and appointment input fields to prevent blank or invalid records[cite: 1, 2].


## 4. Non-Functional Requirements
* **NFR-01 (Usability):** The system interface shall allow a receptionist to complete a booking in under 3 simple actions[cite: 1, 3].
* **NFR-02 (Data Integrity):** The system shall preserve appointment data integrity and avoid data corruption during concurrent operations[cite: 1, 3].
* **NFR-03 (Performance):** Search results for patient records shall be retrieved within 2 seconds[cite: 1, 3].
* **NFR-04 (Maintainability):** The codebase shall follow a modular structure suitable for step-by-step enhancements[cite: 1, 2, 3].
* **NFR-05 (Reliability):** The system shall handle user input errors gracefully without crashing[cite: 1, 3].
* **NFR-06 (Testability):** All functional requirements shall be verifiable through reproducible test scripts[cite: 1, 3].


## 5. User Stories
* **US-01:** As a receptionist, I want to search for existing patients quickly, so that I can prevent creating duplicate patient profiles[cite: 1, 2].
* **US-02:** As a receptionist, I want the system to block double-bookings, so that GPs are not scheduled twice for the same time slot[cite: 1, 2].
* **US-03:** As a GP, I want to view my daily consultation schedule, so that I can prepare for patient appointments in advance[cite: 1, 2].
* **US-04:** As a receptionist, I want to cancel an appointment, so that the time slot is immediately available for other patients[cite: 1, 2].
* **US-05:** As a manager, I want to export basic booking reports, so that I can analyze clinic productivity[cite: 1, 2].
* **US-06:** As a GP, I want to view a patient's past appointment history, so that I can provide better continuous care[cite: 1, 2].


## 6. Acceptance Criteria
* **AC-01 (Successful Booking - Positive Path):**
  * **GIVEN** GP Dr. Smith is available at 10:00 AM on Monday[cite: 1]
  * **WHEN** the receptionist creates an appointment for Patient ID 101 at 10:00 AM[cite: 1]
  * **THEN** the system saves the appointment, changes status to "Scheduled", and marks 10:00 AM as booked[cite: 1].

* **AC-02 (Duplicate Booking Conflict - Negative Path):**
  * **GIVEN** GP Dr. Smith is already booked at 10:00 AM on Monday[cite: 1]
  * **WHEN** the receptionist attempts to book another patient for Dr. Smith at 10:00 AM on Monday[cite: 1]
  * **THEN** the system blocks the booking and displays a "Time Slot Conflict" error message[cite: 1].

* **AC-03 (Cancellation Process - State Transition):**
  * **GIVEN** an active appointment exists for Patient ID 101 at 2:00 PM[cite: 1]
  * **WHEN** the receptionist updates the status to "Cancelled"[cite: 1]
  * **THEN** the system updates the appointment log and releases the 2:00 PM time slot as available[cite: 1].


## 7. Assumptions and Open Questions
* **Assumption 1:** The application is a desktop application running within the clinic premises[cite: 2].
* **Assumption 2:** Clinic staff share a central database instance to maintain synchronization[cite: 2].
* **Open Question 1:** Do practitioners require separate login permissions from receptionists[cite: 1]?
* **Open Question 2:** What specific date range should operational reports cover by default (e.g., weekly vs monthly)[cite: 1, 2]?


## 8. AI Requirements Review Record

| AI Suggestion | Evidence? | Decision | Reason | Verification |
| :--- | :--- | :--- | :--- | :--- |
| **Replace "basic summary reports" in FR-06** with a more specific description because "basic" is ambiguous. | Yes | Accept | The requirement can be interpreted differently by different stakeholders. | Requirement updated and reviewed with management. |
| **Clarify what information should be displayed** when a patient record is found in FR-01. | No, requires validation | Pending | The requirements do not specify the details shown after a search. | Confirm with client and update FR-01 if needed. |
| **Clarify whether duplicate booking prevention** applies only to doctors or also to patients with overlapping appointments. | No, requires validation | Pending | FR-02 only mentions doctors; scope for patient conflicts is unclear. | Confirm business rule with client. |
| **Clarify whether "Completed" and "Cancelled"** are the only appointment statuses required in FR-04. | No, requires validation | Pending | Additional statuses may exist, but they are not specified in the requirements. | Validate with client. |
| **Replace NFR-02 wording** "simple enough for new receptionists to use with zero training" with a measurable usability criterion. | Yes | Accept | The requirement is subjective and difficult to test objectively. | Updated NFR contains measurable success criteria. |
| **Clarify which specific reports** management requires for FR-06. | No, requires validation | Pending | The requirements do not identify the contents of the reports. | Confirm report requirements with management. |
| **Clarify expected behaviour for NFR-03** when the application closes unexpectedly. | No, requires validation | Pending | "Prevent data loss" does not define what recovery outcome is expected. | Confirm recovery expectations with client. |
| **Clarify what is meant by "clinic performance"** in US-03. | Yes | Accept | The term is vague and may have multiple interpretations. | User story updated with specific objective. |
| **Add acceptance criteria** for searching patient records (FR-01). | Yes | Accept | FR-01 is testable, but no acceptance criteria currently verify it. | New Given-When-Then test created. |
| **Ensure practitioner access to appointment history** is explicitly addressed because it appears in stakeholder needs but not clearly in requirements. | No, requires validation | Pending | Stakeholder need mentions appointment history, but practitioner access is not explicitly stated. | Confirm with stakeholder and update requirements if necessary.


## Reflection

During the Stage 2 requirements analysis, the AI review identified several critical ambiguities that I initially missed[cite: 3]. Most notably, it pointed out non-testable phrasing like "basic summary reports" in FR-06 and "simple enough with zero training" in NFR-02, both of which lacked clear, measurable success criteria[cite: 3]. It also caught a gap between stakeholder needs and functional requirements: practitioner access to patient appointment history was listed as a need but lacked explicit mention in the functional requirements[cite: 2, 3].

However, the AI also exhibited overreach by attempting to expand scope beyond the client brief[cite: 2, 3]. It repeatedly flagged questions regarding crash recovery procedures, patient-side double-booking prevention, and complex report schemas—none of which were requested by SmartCare management, who explicitly requested a simple, manageable prototype[cite: 2, 3].

As a result of this review, **FR-06** changed significantly from a vague "basic reports" requirement to a defined specification detailing appointment totals, cancellations, and status breakdowns by practitioner.

This exercise highlighted why software requirements must strictly rely on evidence[cite: 3]. Without evidence-based grounding, AI suggestions can easily introduce scope creep, over-engineer simple systems, or misinterpret client expectations, leading to wasted engineering effort[cite: 2, 3].