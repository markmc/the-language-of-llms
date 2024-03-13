
reveal.js-master/index.html: reveal.js-master index.html.jinja generate.py terms.txt
	python generate.py > reveal.js-master/index.html

reveal.js-master: reveal.js-master.zip
	unzip reveal.js-master.zip
	touch reveal.js-master

reveal.js-master.zip:
	curl -L -o reveal.js-master.zip https://github.com/hakimel/reveal.js/archive/master.zip

open:
	xdg-open reveal.js-master/index.html

clean:
	rm -rf reveal.js-master reveal.js-master.zip
