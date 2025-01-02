import os, shutil

from textnode import TextType, TextNode


def main():
    public_dir = "./public"
    static_dir = "./static"
    check_for_path(public_dir)
    delete_public_files(public_dir)
    copy_files_to_dst(static_dir, public_dir)





    





def delete_public_files(path):
    # check if path exists
    if not os.path.exists(path):
        os.mkdir(path)
        return
    try:
        shutil.rmtree(path)
    except Exception:
        print(f"Unable to delet {path}")
    # if not empty, shutil.rmtree() 
    os.mkdir(path)


    # list of filenames = os.listdir(folder)
    # os.path.join(path, paths) to create a path to a file??
    # os.path.isfile() verifies that path is a file
    # os.path.isdir() verifies that path is a dir
    # os.mkdir(path) creates dir
    # shutil.copy(src, dst) copies the file src to the file/dir dst
        # if dst is dir only, filename will be copied
def copy_files_to_dst(origin_path, dst_path):
    files = os.listdir(origin_path)
    if len(files) == 0:
        return
    check_for_path(dst_path)
    for file in files:
        file_path = os.path.join(origin_path, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dst_path)
        if os.path.isdir(file_path):
            new_dir = os.path.join(dst_path, file)
            os.mkdir(new_dir)
            copy_files_to_dst(file_path, new_dir)

def check_for_path(path):
    if not os.path.exists(path):
        raise Exception(f"Path to {path} is missing")


main()
