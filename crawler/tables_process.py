import csv


class Grades():
    def __init__(self, filename):
        self.courses = list()
        self.GPA = 0
        self.name = ''
        self.filename = filename
        self.__csv_to_object()

    def __gpa_calculate(self, type):
        total_score = 0
        total_credit = 0
        if type == 1:
            for course in self.courses:
                if course['score'] != '免修' and course['property'] != '任选' and course['score'] != '通过':
                    # print(course['name_cn'] + ' ' + course['credit'] + ' ' + course['score'])
                    total_credit += float(course['credit'])
                    total_score += float(course['score']) * float(course['credit'])
        elif type == 2:
            for course in self.courses:
                if course['score'] != '免修' and course['score'] != '通过':
                    # print(course['name_cn'] + ' ' + course['credit'] + ' ' + course['score'])
                    total_credit += float(course['credit'])
                    total_score += float(course['score']) * float(course['credit'])
        return total_score/total_credit

    def get_gpa_required(self):
        return self.__gpa_calculate(1)

    def get_gpa_all(self):
        return self.__gpa_calculate(2)

    def __print_all_courses(self):
        for course in self.courses:
            print(course)

    def __csv_to_object(self):
        try:
            with open(self.filename, 'r') as t:
                lines = csv.reader(t)
                lines = list(lines)
                courses = list()
                for i in range(1, len(lines)):
                    temp = dict()
                    temp['course_num'] = lines[i][0]
                    temp['course_seq'] = lines[i][1]
                    temp['name_cn'] = lines[i][2]
                    temp['name_en'] = lines[i][3]
                    temp['credit'] = lines[i][4]
                    temp['property'] = lines[i][5]
                    temp['score'] = lines[i][6]
                    temp['reason'] = lines[i][7]
                    courses.append(temp)
                self.courses = courses
        except Exception as e:
            print('csv to object error: ' + str(e))
