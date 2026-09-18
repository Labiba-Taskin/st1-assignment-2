## 1. Requirement-to-Concept Trace
| Requirement | Concept | State/behaviour | Decision |
| :--- | :--- | :--- | :--- |
| **FR-01** (Patient Search/Register) | `Patient` | `patient_id`, `name`, `phone` / `update_details()` | Retained as core domain entity. |
| **FR-02** (Prevent Duplicate Bookings) | `Appointment` | `time_slot`, `status` / `is_conflicting()` | Enforced via `Appointment` validation logic. |
| **FR-03** (Real-time GP Schedules) | `Practitioner` | `practitioner_id`, `name`, `schedule` / `get_availability()` | Retained as core domain entity. |
| **FR-04** (Appointment Statuses) | `Appointment` | `status` (Scheduled, Completed, Cancelled, No-Show) / `update_status()` | Encapsulated within `Appointment`. |
| **FR-05** (Free Time Slot on Cancellation) | `Appointment` | `status` / `cancel()` | Releases time slot on status change. |
| **FR-06** (Operational Reports) | `ClinicSystem` | `appointment_list` / `generate_report()` | System controller class handles reporting. |
| **FR-08** (Immutable Appointment History) | `Patient` & `Appointment` | `appointment_history` / `get_history()` | Association link between `Patient` and past `Appointment`s. |

---

## 2. CRC Cards

### Patient
* **Responsibilities:**
  * Maintain demographic details (ID, name, contact info).
  * Maintain personal appointment history log.
* **Collaborators:** `Appointment`.

### Practitioner
* **Responsibilities:**
  * Maintain practitioner profile details (ID, name, specialization)[cite: 4, 5].
  * Manage availability and consultation schedule[cite: 4, 5].
* **Collaborators:** `Appointment`[cite: 4, 5].

### Appointment
* **Responsibilities:**
  * Link a specific `Patient` and `Practitioner` to a designated date and time slot[cite: 4, 5].
  * Track booking status (Scheduled, Completed, Cancelled, No-Show)[cite: 4, 5].
  * Enforce non-overlapping schedule constraints[cite: 4, 5].
* **Collaborators:** `Patient`, `Practitioner`[cite: 4, 5].

### ClinicSystem (Optional / Controller Class)
* **Responsibilities:**
  * Coordinate patient search, appointment bookings, and cancellations[cite: 4, 5].
  * Compile basic operational reports on clinic activity[cite: 4, 5].
* **Collaborators:** `Patient`, `Practitioner`, `Appointment`[cite: 4, 5].

---

## 3. UML Class Diagram

```text
+-----------------------+                   +-----------------------------------+                   +---------------------------+
|        Patient        |                   |            Appointment            |                   |        Practitioner       |
+-----------------------+                   +-----------------------------------+                   +---------------------------+
| - patient_id: String  | 1               * | - appointment_id: String          | *               1 | - practitioner_id: String |
| - name: String        |-------------------| - date_time: DateTime             |-------------------| - name: String            |
| - phone: String       |  has history      | - status: AppointmentStatus       |  assigned to      | - specialization: String  |
+-----------------------+                   +-----------------------------------+                   +---------------------------+
| + update_details()    |                   | + cancel()                        |                   | + get_schedule()          |
| + get_history()       |                   | + update_status(new_status)       |                   | + check_availability()    |
+-----------------------+                   +-----------------------------------+                   +---------------------------+
                                                              ^
                                                              | manages
                                                  +-----------------------+
                                                  |     ClinicSystem      |
                                                  +-----------------------+
                                                  | - patient_records     |
                                                  | - appointment_records |
                                                  +-----------------------+
                                                  | + book_appointment()  |
                                                  | + generate_report()   |
                                                  +-----------------------+
                                                  
## 4. Design Rationale

* **Class Selection:** Core classes (`Patient`, `Practitioner`, `Appointment`) directly represent the physical entities identified in the SmartCare case study[cite: 2]. An optional `ClinicSystem` controller class was added to centralize workflow operations like reporting and duplicate validation[cite: 1, 2].
* **Multiplicities:**
  * A `Patient` can have zero or many (`0..*`) `Appointment` records over time[cite: 1, 2].
  * A `Practitioner` can be assigned to multiple (`0..*`) `Appointment` slots[cite: 1, 2].
  * Each `Appointment` instance links exactly one (`1`) `Patient` to exactly one (`1`) `Practitioner`[cite: 1, 2].
  
## 5. AI Design Review Record

| AI Suggestion | Evidence | Decision | Reason | Model Change |
| :--- | :--- | :--- | :--- | :--- |
| **Suggest classes only when supported** by one or more approved requirement IDs. | Requirements-to-design traceability practice requires each design element to be justified by documented requirements. | **Accepted** | Prevents unsupported classes and scope creep. | Add requirement ID references (e.g., FR-01, FR-02) to each class in the UML model. |
| **Suggest associations only when interactions** are explicitly described in requirements. | Relationships should represent documented business rules or system interactions. | **Accepted** | Reduces assumptions and improves model accuracy. | Record supporting requirement IDs for every association, aggregation, or composition. |
| **Flag any proposed class, attribute, or method** that lacks requirement evidence. | Untraceable design elements cannot be verified against stakeholder needs. | **Accepted** | Improves auditability and requirements compliance. | Add a traceability review step before finalizing the class diagram. |
| **Distinguish between confirmed design elements and assumptions.** | Requirements engineering standards recommend separating verified requirements from assumptions. | **Accepted** | Prevents stakeholders from treating assumptions as approved requirements. | Add an "Assumption" note to model elements without requirement support or exclude them from the baseline design. |

## 6. Reflection

The hardest part of the domain modeling process was determining the correct boundaries and responsibilities for each class while maintaining strict requirement traceability[cite: 2]. Initially, deciding where to place appointment conflict checks and availability schedules created confusion[cite: 2]. It was tempting to assign system-wide validation duties directly to the `Practitioner` entity[cite: 1, 2]. However, analyzing the business rules revealed that checking for overlapping bookings requires global visibility over all clinic schedules[cite: 2]. Adding this logic to `Practitioner` would have overloaded the class with controller responsibilities[cite: 1, 2].

During the design review, the AI over-designed the domain model by suggesting complex enterprise classes such as `BillingSystem`, `PatientInsurance`, and `NotificationService`[cite: 2]. While these classes are standard in large-scale healthcare applications, none of them had supporting evidence in the SmartCare v0.2 functional requirements[cite: 2]. 

To prevent scope creep, every proposed design element was validated against the explicit requirements[cite: 2]. Evidence from FR-01 through FR-10 supported keeping `Patient`, `Practitioner`, and `Appointment` as lean core entities, while introducing a lightweight `ClinicSystem` controller class to manage central workflows like reporting and booking validation[cite: 1, 2].