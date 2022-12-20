import pytest
import matplotlib.pyplot as plt
from generate_password import PasswordGenerator


@pytest.mark.parametrize('word_list, plot_name', [
    (PasswordGenerator().adjectives, 'adjectives'),
    (PasswordGenerator().nouns, 'nouns')
])
def test_get_random_adjectives(word_list, plot_name):
    pw_gen = PasswordGenerator()
    freqs = {}
    for i in range(1_000_000):
        try:
            word = pw_gen.get_random(word_list)
            freqs[word] = freqs.get(word, 0) + 1
        except:
            print('Error!!')

    sorted_freqs = sorted(freqs.values(), reverse=True)

    assert sorted_freqs[0] * 0.5 < sorted_freqs[-1] < sorted_freqs[0] * 1.5
    assert set(freqs.keys()) == set(word_list)

    # Generate sorted frequency plot
    plt.plot(sorted_freqs)
    plt.title(f'Sorted frequency of selected {plot_name}')
    plt.xlabel('Word number')
    plt.ylabel('Absolute frequency')
    plt.savefig(f'report/Frequency of {plot_name}.png', dpi=600)
    plt.close()


if __name__ == '__main__':
    import entropy

    test_get_random_adjectives(PasswordGenerator().adjectives, 'adjectives')
    test_get_random_adjectives(PasswordGenerator().nouns, 'nouns')
