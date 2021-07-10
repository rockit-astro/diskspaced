RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba observatory-diskspace-server.spec
	${RPMBUILD} -ba observatory-diskspace-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-diskspace.spec
	${RPMBUILD} -ba onemetre-diskspace-data.spec
	${RPMBUILD} -ba clasp-diskspace-data.spec
	${RPMBUILD} -ba superwasp-diskspace-data.spec
	mv build/noarch/*.rpm .
	rm -rf build

