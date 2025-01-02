from copy_static import delete_public_files, copy_files_to_dst, check_for_path
from textnode import TextType, TextNode


def main():
    public_dir = "./public"
    static_dir = "./static"
    print("Deleting public directory...")
    check_for_path(public_dir)
    delete_public_files(public_dir)
    print("Copying static files to the public directory...")
    copy_files_to_dst(static_dir, public_dir)





    







main()
