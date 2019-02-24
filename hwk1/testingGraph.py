from random import randint
from csp import min_conflicts, CSP

def create_room_timelist(timeslots, roomlist):
    timelist = []
    for i in timeslots:
        for v in roomlist:
            timelist.append([v, i])

    return timelist


def generate_schedule_domain(assign_list, room_time_list):
    sched_domain = {}
    for key in assign_list:
        for v in room_time_list:
            v_copy = v[:]
            v_copy.append(assign_list[key])
            if key not in sched_domain:
                sched_domain[key] = [v_copy]
            else:
                sched_domain[key].append(v_copy)
    return sched_domain


def create_course_neighbors(some_courses):
    course_neighbors = []
    for i in some_courses:
        for v in some_courses:
            if i != v:
                course_neighbors.append([i, v])
    return course_neighbors


def different_fac_time_constraint(A, a, B, b):
    if a[3] == b[3]:
        return False
    if a[1] == b[1] and a[2] == b[2]:
        return False
    return True


if __name__ == "__main__":

    courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs262', 'cs384']
    faculty = ['adams', 'hplantin', 'kvlinden', 'dschuurman', 'vtn2']
    assignments = {'cs108': 'dschuurman', 'cs112': 'adams', 'cs212': 'hplantin', 'cs214': 'adams', 'cs232': 'vtn2',
                   'cs262': 'kvlinden', 'cs384': 'dschuurman'}
    times = ['mwf0900', 'mwf1030', 'mwf1130', 'tt1500', 'tt1300']
    rooms = ['nh253', 'sb382']

    time_list = create_room_timelist(times, rooms)
    domain = generate_schedule_domain(assignments, time_list)
    neighbors = create_course_neighbors(courses)
    print("Variables: " + str(courses))
    print("Domains: " + str(domain))
    print("Neighbors: " + str(neighbors))

    schedule = min_conflicts(CSP(courses, domain, neighbors, different_fac_time_constraint))
    if schedule is None:
        print('No valid schedule could be made with given constraints.')
    else:
        print(schedule)




