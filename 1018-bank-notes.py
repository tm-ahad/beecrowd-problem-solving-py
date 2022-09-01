n = int(input())
print(n)
note_list = ['100', '50', '20', '10', '5', '2', '1']
remain = n

for notes in note_list:
    note_val = f"{notes},00"
    notes = int(notes)
    note_count = int((remain - (remain % notes))/notes)
    res = f"{note_count} nota(s) de R$ {note_val}"
    remain = remain - (note_count * notes)
    print(res)
