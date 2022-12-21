## Add your own custom Makefile targets here
.PHONY: validate-with-linkml

RUN = poetry run

validate-with-linkml: src/no_corners/schema/no_corners.yaml src/data/examples/BiosampleCollection.yaml
	$(RUN) linkml-validate \
	  --target-class BiosampleCollection \
	  --schema $^
