MODULE=tsygFort
SOURCES=geopack08.for T96.f T02.f

all: $(SOURCES) $(MODULE)



#	$(FC) -w -O2 -fbacktrace -fno-automatic -fPIC -c geopack08.for T96.f T02.f

$(MODULE): $(SOURCES)
	f2py --overwrite-signature $^ -m $@ -h geopack08.pyf
	f2py --quiet --f77flags="-std=legacy" -c geopack08.pyf $^

install:
	mv $(MODULE)*.so ..

clean:
	$(RM) *.o *.so
#"*.pyf"
