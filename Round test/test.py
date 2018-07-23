import os
import argparse
import timeit
import difflib

def readfile(filename):
    try:
        with open(filename, 'r') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()

def diff_file(filename1, filename2):
    text1_lines = readfile(filename1)
    text2_lines = readfile(filename2)
    if text1_lines != text2_lines:
        d = difflib.HtmlDiff()
        result = d.make_file(text1_lines, text2_lines, filename1, filename2, context=False)
        with open('result.html', 'w') as resultfile:
            resultfile.write(result)
        return False
    return True

def main(args):
    if args.std_file_path != None:
        if '.cpp' not in args.file_path:
            print 'your code file isnot a standard cpp file, please check your input'
            exit(-1)
        if '.cpp' not in args.std_file_path:
            print 'std code file isnot a standard cpp file, please check your input'
            exit(-1)
        if args.gen_script_path == None:
            print 'please input a data generator, both cpp & python is ok'
            exit(-1)

        os.system('g++ ' + args.file_path + ' -o ' + args.file_path[:-4] + ' -std=c++11 -static -O2 -DONLINE_JUDGE')
        os.system('g++ ' + args.std_file_path + ' -o ' + args.std_file_path[:-4] + ' -std=c++11 -static -O2 -DONLINE_JUDGE')
        if '.cpp' in args.gen_script_path:
            os.system('g++ ' + args.gen_script_path + ' -o ' + args.gen_script_path[:-4] + ' -std=c++11 -static -O2 -DONLINE_JUDGE')
        
        std_output_file_path = args.output_file_path[:-4] + '_std.txt'
        std_time = 0.0
        your_time = 0.0
        print 'Round = %d' %(args.check_round)
        for i in range(args.check_round):
            if '.cpp' in args.gen_script_path:
                os.system(args.gen_script_path[:-4])
            else:
                os.system('python ' + args.gen_script_path)
            start_time = timeit.default_timer()
            os.system(args.file_path[:-4] + ' <' + args.input_file_path + ' >' + args.output_file_path)
            mid_time = timeit.default_timer()
            os.system(args.std_file_path[:-4] + ' <' + args.input_file_path + ' >' + std_output_file_path)
            end_time = timeit.default_timer()

            ret = diff_file(args.output_file_path, std_output_file_path)
            if ret == False:
                print 'error at Round %d, result at \'result.html\'' %(i + 1)
                exit(-2)

            your_time += mid_time - start_time
            std_time += end_time - mid_time

        your_time /= args.check_round
        std_time /= args.check_round
        print 'AC\nyour average exec time : %f s\nstd  average exec time : %f s' %(your_time, std_time)
    else:
        if '.cpp' not in args.file_path:
            print 'not a standard cpp file, please check your input'
            exit(-1)
        
        os.system('g++ ' + args.file_path + ' -o ' + args.file_path[:-4] + ' -std=c++11 -static -O2 -DONLINE_JUDGE')
        start_time = timeit.default_timer()
        if args.input_file_path != None and args.output_file_path != None:
            os.system(args.file_path[:-4] + ' <' + args.input_file_path + ' >' + args.output_file_path)
        elif args.input_file_path != None:
            os.system(args.file_path[:-4] + ' <' + args.input_file_path)
        elif args.output_file_path != None:
            os.system(args.file_path[:-4] + ' >' + args.output_file_path)
        else:
            os.system(args.file_path[:-4])
        end_time = timeit.default_timer()
        print 'exec time = %f s\n' %(end_time - start_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action = 'store', nargs = '?',
                        dest = 'file_path',
                        help = 'input your cpp file')
    parser.add_argument('-s', '--std', action = 'store', nargs = '?',
                        dest = 'std_file_path',
                        help = 'input std cpp file for verification')   
    parser.add_argument('-i', '--input', action = 'store', nargs = '?',
                        dest = 'input_file_path',
                        help = 'input the program\'s input file, redirect the stdin')
    parser.add_argument('-o', '--output', action = 'store', nargs = '?',
                        dest = 'output_file_path',
                        help = 'output file path for necessary.')
    parser.add_argument('-g', '--gen_script', action = 'store', nargs = '?',
                        dest = 'gen_script_path',
                        help = 'data generator script path, must be python script or cpp file, and your generator must output to the input file that you given by -i arg')
    parser.add_argument('-r', '--round', action = 'store', nargs = '?', type = int, default = 100,
                        dest = 'check_round',
                        help = 'check round for verification, 100 for default, include data generation, run both your code and std code and verify their output.')
    
    args = parser.parse_args()
    main(args)