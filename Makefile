DIST?=.el7.centos
MOCK=planex-cache --cachedirs=/rpmcache
FETCH_EXTRA_FLAGS=--mirror file:///distfiles/ocaml2
RPM_EXTRA_DEFINES=--define "_sourcedir %_topdir/SOURCES/%name"

include /usr/share/planex/Makefile.rules

