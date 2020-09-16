# User Input
reversible1 = input("Please enter a sentence: ")
reversible2 = input("Please enter another sentence: ")
reversible3 = input("Please enter another sentence: ")

#Giving the user a choice
reverse_or_no = input(""" Do you want to, not only reverse the order of the sentences, but also reverse the letters or not?
If you want to reverse the order, press s.
If you want to keep it the same, press a.
> """)

#If's on choice
if reverse_or_no == 'a':
    lowercase = input("""Do you want to lowercase your sentences?
To do so, press d.
> """)
    if lowercase == 'd':
        normal_lowercase = [x.lower() for x in[reversible1, reversible2, reversible3]]
        print(normal_lowercase)
if reverse_or_no == 's':
    lowercase = input("""Do you want to lowercase your sentences?
To do so, press d.
> """)
    if lowercase == 'd':
        reversed1 = reversible1[::-1]
        reversed2 = reversible2[::-1]
        reversed3 = reversible3[::-1]
        reversing_lowercase =[x.lower() for x in[reversed1, reversed2, reversed3]]
        print(reversing_lowercase)
    
    
