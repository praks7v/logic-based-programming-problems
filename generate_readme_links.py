import os


def generate_file_links(target_folder):
    file_links = []

    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Use the file name (without extension) as the link text
        link_text = os.path.splitext(file)[0].replace("_", " ").title()

        # Convert spaces to %20 for URL-friendliness
        url_friendly_path = file.replace(" ", "%20")

        file_link = f"- [{link_text}]({url_friendly_path})"
        file_links.append(file_link)

    return file_links


if __name__ == "__main__":
    target_folder = "/home/anaya/PycharmProjects/logic_based_programming_problems/logic-based-programming-problems"
    links = generate_file_links(target_folder)

    with open("README.md", "w") as readme_file:
        readme_file.write("\n".join(links))
