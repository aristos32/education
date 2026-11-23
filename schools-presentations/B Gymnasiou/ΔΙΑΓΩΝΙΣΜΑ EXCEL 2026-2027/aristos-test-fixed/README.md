# Διαγώνισμα Excel — Β΄ Γυμνασίου (Β4.1 Μ1–Μ14)

Fixed version of the Excel practical test. Γυμνάσιο Ζακακίου, Α΄ Τετράμηνο 2026–2027, 40΄, 20 marks.

## Files

| File | Contents |
| --- | --- |
| `Διαγώνισμα.xlsx` | The fixed test. Students open this file. The name matches step 1. |
| `1_Pinakas_Prodiagrafon_Excel_B_Gym.docx` | Πίνακας Προδιαγραφών: each task with its Β4.x indicators, the split by unit and by cognitive level, and the M1–M14 indicators the test doesn't cover |
| `2_Odigos_Diorthosis_Excel_B_Gym.docx` | Οδηγός Διόρθωσης: general marking rules, then for each task what to check, partial marks and common mistakes |
| `3_Lyseis_Excel_B_Gym.docx` | Λύσεις: expected formulas, values and steps for each task |
| `4_Critique_Excel_Test_B_Gym.docx` | Critique of the original test. Most of its "fix before the test" items are now done (see below). |

All sheets, the pie chart and the team logos are the same as in the original file.

## Changes to the test (`Διαγώνισμα.xlsx`)

### Fixes
- **Save step added.** New item 22: «Να αποθηκεύσετε το αρχείο (Ctrl+S) και να κλείσετε το Excel (δεν βαθμολογείται)». «Καλή Επιτυχία!!!» moved down one row.
- **Score box.** The broken `=SUM(#REF!)` in cell M3 of the Βαθμός sheet is removed. The box next to «Βαθμός:» is now empty on the printed paper.
- **Question 16.** The COUNT range changed from `A1:H10` to **`B4:E10`**. The answer is always **28** and no longer depends on question 15.
- **Τύποι sheet.** The leftover hint cells J12:J13 are removed («ΘΑ ΠΡΕΠΕΙ ΝΑ ΧΡΗΣΙΜΟΠΟΙΗΘΕΙ ΑΠΟΛΥΤΗ ΑΝΑΦΟΡΑ $…» and «Αναζητήστε "absolute reference" στη βοήθεια»).
- **Question 10.** Students now delete **column G (the second «Βαθμός» column)** instead of the empty column F, so a wrong or missing deletion is easy to see.
- **Question 18.** It now says to *change* the title from «Chart Title» to "NBA 2024-2025", because the chart already has a placeholder title.

### Wording
- «desctop» → desktop.
- Added the missing «Να»: «Να ανοίξετε», «να συμπληρώσετε το όνομά σας», «Να αντιγράψετε», «να γράψετε», «να εισαγάγετε».
- «στη περιοχή» → «στην περιοχή». «την στήλη» → «τη στήλη».
- Question 17 now has a verb: «…να γράψετε τη συνάρτηση που στρογγυλοποιεί χωρίς δεκαδικά τον Μέσο Όρο Εβδομάδας (B14).»
- Cell references are now typed with Latin letters, not Greek: A1, A2:G20, A2:A6, A1:I1, H4, B14.

## Changes to the Word documents
- **Question 10:** the marking guide and solutions now refer to deleting column G (the average ends up in E24 only).
- **Question 16:** the answer is `=COUNT(B4:E10)` → 28. Marking is 0.5 for the right function and 0.5 for the right range.
- **Question 18:** describes changing the existing «Chart Title».
- **Step 22:** listed as ungraded, with a reminder to check that every student saved.

## Not changed (your decision)
- Question 13 still says «Χρησιμοποιήστε Απόλυτη αναφορά ($)».
- Every question is still worth 1 mark. The marking guide splits the mark inside multi-part questions.
- The time is still 40 minutes.
- No questions were added for AutoFit, cell Fill Color or Move/Copy sheet.
- Question 14 still doesn't ask for percentage format. Decimals are accepted.

## Note
The online doc «Διαγώνισμα Excel Β΄ Γυμνασίου — Πίνακας Προδιαγραφών, Οδηγός Διόρθωσης, Λύσεις» still has the **old** answers for questions 10 and 16. Use the Word files.
