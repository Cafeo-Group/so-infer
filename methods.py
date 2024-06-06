from sys import stdin
from datetime import datetime
from random import shuffle
import csv

def get_samples() -> list:
    '''Reads samples from stdin and returns a list of tuples with the samples.'''
    samples = []
    for line in stdin: 
        samples.append(tuple(line.strip().split(',')))
    return samples

def get_samples_from_csv(file: str) -> list:
    '''Reads samples from a csv file and returns a list of tuples with the samples.'''
    samples = []
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)

        ##Skips the header
        next(csv_reader)
        
        for row in csv_reader:
            samples.append(tuple(row))
    return samples

def filter_by_date(samples: list, date_start: datetime, date_end: datetime) -> list:
    '''Filters samples by date and returns a list of tuples with the samples that are within the date range.'''
    desired = []
    for sample in samples:
        date = datetime.fromisoformat(sample[3])
        if date >= date_start and date <= date_end:
            desired.append(sample)
    return desired

def get_answered(samples: list) -> list:
    '''Returns a list of tuples with the code samples that have an accepted answer.'''
    desired = []
    for sample in samples:
        if sample[6] == '':
            desired.append(sample)
    return desired

def get_unanswered(samples: list) -> list:
    '''Returns a list of tuples with the samples that do not have an accepted answer.'''
    desired = []
    for sample in samples:
        if sample[6] != '':
            desired.append(sample)
    return desired

def split_samples(samples: list) -> tuple:
    '''Splits the samples into two lists: one with the answered samples and another with the unanswered samples.'''
    answered = get_answered(samples)
    unanswered = get_unanswered(samples)
    return answered, unanswered

def cut_by_limit(samples: list, limit: int) -> list:
    '''Cuts the samples list by the limit specified. It will remove the samples that exceed the limit for each path.
    Still under development.
    '''
    path_len_dict = {}
    for sample in samples:
        # if sample[1] not in path_len_dict:
        #     path_len_dict[sample[1]] = 0
        # elif sample[1] in path_len_dict and path_len_dict[sample[1]] <= limit:
        #     path_len_dict[sample[1]] += 1
        # else:
        #     print(sample[1],count)
            samples.remove(sample)
    return samples

def get_path(samples: list) -> set:
    '''Returns a set with the paths of the samples.'''
    categories = set()
    for sample in samples:
        categories.add(sample[1])
    return categories

def get_by_path(samples: list, path: str, limit_for_path: int=None) -> list:
    '''Returns a list of tuples with the samples that have the specified path.'''
    desired = []
    shuffle(samples)
    for sample in samples:
        if sample[1] == path:
            desired.append(sample)
    
    if limit_for_path == None:
        return desired
    else:
        cut = cut_by_limit(desired, limit_for_path)
        return cut

def create_csv_with_samples(samples: list, file: str):
    '''Creates a csv file with the samples. The file will have the following columns: framework, path, id, creationDate, ownerUserId, postTypeId, acceptedAnswerId.'''
    with open(file, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['framework', 'path', 'id', 'creationDate', 'ownerUserId', 'postTypeId', 'acceptedAnswerId'])
        for sample in samples:
            csv_writer.writerow(sample)