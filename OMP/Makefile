CXX=icpc
CXXFLAGS=-c -qopenmp -qopt-report=5 -xMIC-AVX512
LDFLAGS=-qopenmp

OBJECTS=ParallelOMPMostCommonAncester.o 

all: app

app: $(OBJECTS)
	$(CXX) $(LDFLAGS) -o app $(OBJECTS)

queue: all
	echo 'cd $$PBS_O_WORKDIR ; ./app' | qsub -N process_omp

clean:
	rm *.o app process_omp.*
