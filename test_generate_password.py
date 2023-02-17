import pytest

import os
import matplotlib.pyplot as plt
from generate_password import PasswordGenerator


@pytest.mark.parametrize('word_list, plot_name', [
    (PasswordGenerator().wl.adjectives, 'adjectives'),
    (PasswordGenerator().wl.nouns, 'nouns')
])
def test_get_random_adjectives(word_list, plot_name):
    pw_gen = PasswordGenerator()
    freqs = {}
    

    for _ in range(1_000_000):
        try:
            word = pw_gen.get_random(word_list)
            freqs[word] = freqs.get(word, 0) + 1
        except:
            print('Error!!')

    sorted_freqs = sorted(freqs.values(), reverse=True)

    # Generate sorted frequency plot
    if not os.path.exists('report'):
        os.mkdir('report')

    plt.plot(sorted_freqs)
    plt.title(f'Sorted frequency of selected {plot_name}')
    plt.xlabel('Word number')
    plt.ylabel('Absolute frequency')
    plt.savefig(f'report/Frequency of {plot_name}.png', dpi=600)
    plt.close()

    # Skip tests if word lists are too long.
    mini, maxi = 0.5, 1.5
    if len(pw_gen.wl.adjectives) > 10_000 or len(pw_gen.wl.nouns) > 10_000:
        mini, maxi = 0.01, 100

    assert sorted_freqs[0] * mini < sorted_freqs[-1] < sorted_freqs[0] * maxi
    assert set(freqs.keys()) == set(word_list)


if __name__ == '__main__':
    import entropy

    test_get_random_adjectives(PasswordGenerator().wl.adjectives, 'adjectives')
    test_get_random_adjectives(PasswordGenerator().wl.nouns, 'nouns')
