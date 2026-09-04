| Question | Human version | AI version |
|---|---|---|
| Easy to understand? | Yes, simple list and dict | No, added extra functions, file handling and menus |
| Runs successfully? | Yes | Yes, but needs more setup and is more complex |
| Uses only required features? | Yes, no database/GUI | No, suggested database, datetime module and file save |
| Adds assumptions? | No | Yes, assumed I need a menu system and file persistence |
| Handles errors? | Only checks empty patient name | Yes, checks date format, duplicate times, and empty fields |
| Could I explain it? | Yes | No, too complex for beginner level |

Five limitations I found:
1. No validation for date format
2. No check for duplicate appointments
3. Data disappears when program closes (no file save)
4. No way to delete or update an appointment
5. No check for empty practitioner name
