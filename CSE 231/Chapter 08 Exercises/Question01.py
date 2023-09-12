def music_func(music= "Classic Rock",group= "The Beatles",singer = "Freddie Mercury"):
    print("The best kind of music is", music)
    print("The best music group is", group)
    print("The best lead vocalist is", singer)
    
def main():
    music, group, singer = input().split(',')
    music_func(music, group, singer)
    music_func()
main()