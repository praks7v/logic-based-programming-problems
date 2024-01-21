def check_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    result = check_anagrams(string1, string2)
    if result:
        print(f"{string1} and {string2} are anagrams.")
    else:
        print(f"{string1} and {string2} are not anagrams.")
