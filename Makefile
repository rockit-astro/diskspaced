RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba onemetre-diskspace-server.spec
	${RPMBUILD} -ba rasa-diskspace-server.spec
	${RPMBUILD} -ba observatory-diskspace-client.spec
	mv build/noarch/*.rpm .
	rm -rf build

