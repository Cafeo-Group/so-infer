from methods import filter_by_date, get_samples_from_csv, split_samples, get_path, get_by_path, create_csv_with_samples
from datetime import datetime

def main():
    samples = filter_by_date(get_samples_from_csv('initSampleQuestions.csv'), datetime.fromisoformat('2023-01-01'), datetime.fromisoformat('2024-06-05'))
    answered, unanswered = split_samples(samples)

    paths_in_both = get_path(answered) & get_path(unanswered)    
    by_path = []
    for path in paths_in_both:
        by_path.extend(get_by_path(samples, path, None))
    ans_by_path, uns_by_path = split_samples(by_path)

    print(f'Total code samples from period: {len(samples)}')
    print(f'Total samples in both paths {len(by_path)}')
    print(f'Answered from paths: {len(ans_by_path)}')
    print(f'Unanswered from paths: {len(uns_by_path)}')
    print(f'Total of paths present in both: {len(paths_in_both)}')
    print(f'List of paths in both: {paths_in_both}')

    create_csv_with_samples(by_path, 'samplesInBothPaths.csv')
    print('\n--------------------------------------------------\n'
          +' CSV file created with the samples in both paths.\n'
          +'--------------------------------------------------\n')