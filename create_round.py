import os
import sys
import shutil

def template(filepath):
    if os.path.exists('template.cpp'):
        shutil.copy('template.cpp', filepath)

def main():
    try:
        contest_dir_path = 'Round ' + sys.argv[1]
        problem_num = int(sys.argv[2])
    except IndexError:
        print 'Usage: python create_round.py <contest_round> <problem_number>\n \
               create a folder named \'Round <contest_round>\' contains <problem_number> serialized empty cpp files\n \
               you can also call template function to add your own headers to your cpp file.\n'
        return -1
    else:
        if not os.path.exists(contest_dir_path):
            os.mkdir(contest_dir_path)
            for i in range(1, problem_num + 1):
                filename = str(1000 + i) + '.cpp'
                open(os.path.join(contest_dir_path, filename), 'w')
                template(os.path.join(contest_dir_path, filename))
            if os.path.exists('test.py'):
                shutil.copy('test.py', os.path.join(contest_dir_path, 'test.py'))
            open(os.path.join(contest_dir_path, 'in.txt'), 'w')
            open(os.path.join(contest_dir_path, 'std.cpp'), 'w')
            open(os.path.join(contest_dir_path, 'gen.py'), 'w')


if __name__ == '__main__':
    main()