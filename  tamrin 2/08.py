students={
    "ali": 18,
    "reza": 15,
    "sara": 19
}
average=(sum(students.values())/len(students))
print("average of scores:",average)
highest_score=(max(students.values()))
print("highest score:",highest_score)
for score in students.values():
    if score <10:
        print("warning!")