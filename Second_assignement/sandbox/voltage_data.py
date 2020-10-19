import numpy
from matplotlib import pyplot as plt


class VoltageData:
    """times and voltages are two iterables of the same lenght"""
    def __init__(self, times, voltages):
        t = numpy.array(times,dtype=numpy.float64)
        v = numpy.array(voltages,dtype=numpy.float64)
        self._data = numpy.column_stack([t,v])     #controlla anche che le lunghezze di t e v siano uguali

    @property    #getter per leggere i tempi da timestamps
    def timestamps(self):
        return self._data[:,0]

    @property    #getter per leggere i voltaggi da voltages
    def voltages(self):
        return self._data[:,1]

    @voltages.setter    #per cambiare i valori dei voltaggi
    def voltages(self, new_values):
        self._data = numpy.column_stack([self.timestamps,new_values])

    def __len__(self):
        """return the number of measurement"""
        return len(self._data)

    def __getitem__(self, index):
        """random access"""
        return self._data[index]

    def __iter__(self):
        return iter(self._data)   #fortunatamente numpy itera prima le righe, come serve a noi

    def __str__(self):
        """convert data in strings to print"""
        row_fmt = '{:d}) {:.1f} {:.2f}'
        output_string = [row_fmt.format(i,entry[0],entry[1]) for i,entry in enumerate(self)]
        return '.\n'.join(output_string)

    def plot(self, ax=None, fmt='bo--', **kwargs):
        """plot data with matplotlib.pyplot"""
        if ax is not None:
            plt.sca(ax)
        else:
            plt.figuer('voltages vs time')
        plt.plot(self.timestamps, self.voltages, fmt, **kwargs)
        



if __name__ == '__main__':
    """ Here we test the functionalities of our class. These are not proper
    UnitTest - which you will se in a future lesson."""
    # Load some data
    t, v = numpy.loadtxt("C:\\Users\\e.zippo\\Desktop\\Università\\Magistrale\\Computing_methods\\Second_assignement\\sandbox\\sample_data_file.txt", unpack=True)
    # Thest the constructor
    v_data = VoltageData(t, v)
    # Test len()
    assert len(v_data) == len(t)
    # Test the timestamps attribute
    assert numpy.all(v_data.voltages == v)
    # Test the voltages attribute
    assert numpy.all(v_data.timestamps == t)
    # Test square parenthesis
    assert v_data[3, 1] == v[3]
    assert v_data[-1, 0] == t[-1]
    # Test slicing
    assert numpy.all(v_data[1:5, 1] == v[1:5])
    # Test iteration
    for i, entry in enumerate(v_data):
        assert entry[0] == t[i]
        assert entry[1] == v[i]
    # Test printing
    print(v_data)
    # Test plotting
    plt.figure('voltage vs time')
    v_data.plot(plt.gca())
    plt.show()
