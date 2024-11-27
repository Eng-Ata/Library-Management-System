L = {}
M = {}
A = {}
while True:
    print("لطفاً یکی از گزینه‌های زیر را انتخاب کنید:")
    print("1.اضافه کردن کتاب")
    print("2. ثبت نام در کتابخانه")
    print("3. جستجوی عضو")
    print("4. جستجوی کتاب")
    print("5. امانت گرفتن کتاب")
    print("6. پس دادن کتاب")
    print("7. گزارش کتاب‌های در امانت")
    print("8. گزارش امانت‌های یک عضو ")
    print("9. خروج")
    choice = input("انتخاب کنید (۱-۹): ")
    if choice == "1":
        book = input("نام کتاب را وارد کنید: ")
        L[len(L) + 1] = book
        print("به کتابخانه اضافه شد")
    elif choice == "2":
        name = input("نام عضو وارد کنید: ")
        M[len(M) + 1] = name
        print(" در کتابخانه ثبت شد.")
    elif choice == "3":
        search_member = input("نام عضو را وارد کنید: ")
        if search_member in M.values():
            print(" در کتابخانه وجود دارد.")
        else:
            print("در کتابخانه یافت نشد")
    elif choice == "4":
        search_book = input("نام کتاب را وارد کنید: ")
        if search_book in L.values():
            print("در کتابخانه موجود است.")
        else:
            print("در کتابخانه یافت نشد.")
    elif choice == "5":
        borrow_member = input("نام عضوی که می‌خواهد کتابی به امانت بگیرد را وارد کند: ")
        borrow_book = input("نام کتابی که می‌خواهید به امانت بگیرید را وارد کنید: ")
        if borrow_book in L.values():
            if borrow_book not in A .values():
                A[borrow_member] = borrow_book
                print(f"کتاب '{borrow_book}' توسط '{borrow_member}' به امانت گرفته شد.")
            else:
                print(f"کتاب '{borrow_book}' در حال حاضر به امانت است.")
        else:
            print(f"کتاب '{borrow_book}' در کتابخانه موجود نیست.")
    elif choice == "6":
        return_member = input("نام عضوی که می‌خواهد کتابی را پس بدهد را وارد کنید: ")
        return_book = input("نام کتابی که می‌خواهید پس بدهید را وارد کنید: ")
        if return_member in A and A[return_member] == return_book:
            del A[return_member]
            print(f"کتاب '{return_book}' توسط '{return_member}' پس داده شد.")
        else:
            print(f"کتاب '{return_book}' توسط '{return_member}' به امانت گرفته نشده است.")
    elif choice == "7":
        if A :
            print("گزارش کتاب‌های در امانت:")
            for member, book in A .items():
                print(f"{member} کتاب '{book}' را به امانت گرفته است.")
        else:
            print("هیچ کتابی به امانت گرفته نشده است.")
    elif choice == "8":
        report_member = input("نام عضو وارد کنید: ")
        member_books = [book for member, book in A .items() if member == report_member]
        if member_books:
            print(f"کتاب‌های امانت گرفته شده توسط '{report_member}':")
            for book in member_books:
                print(book)
        else:
            print(" به امانت گرفته نشده است")
    elif choice == "9":
        print("موفق باشید")
        break
    else:
        print("لطفاً یک انتخاب معتبر وارد کنید.")
