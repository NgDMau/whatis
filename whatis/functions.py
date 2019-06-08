def whatis(acronyms:str):
    acronyms = acronyms.lower()
    datafile_path = "/home/andjm/whatis/whatis/acronyms.txt"
    with open(datafile_path,"r") as file:
        data = file.readlines()
    final_result_list = []
    first_letter = acronyms[0]
    matched_list = []
    for word in data:
        if acronyms == word.split(" ")[0]:
            matched_list.append(word)
    if len(matched_list) == 0:
        print("No phrase found!")
    else:
        for matched in matched_list:
            result_list = matched.split("|")
            result_list.remove(result_list[0])
            for result in result_list:
                sparse_list = result.split(" ")
                # remove last 3 elements 
                sparse_list.remove(sparse_list[-1])
                sparse_list.remove(sparse_list[-1])
                sparse_list.remove(sparse_list[-1])
                # check the language
                if sparse_list[-1] == "e":
                    language = " (english)"
                elif sparse_list[-1] == "v":
                    language = " (tiếng Việt)"
                sparse_list.remove(sparse_list[-1])
                final_result = " ".join(sparse_list) + language
                print(final_result)
                final_result_list.append(final_result)
    return final_result_list