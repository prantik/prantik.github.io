### Building Tag Index Pages ###

For security reasons, github doesn't allow running plugins and tag index pages built using `tag_gen.rb` are not served by github. A hack around this is to build to the tag index pages locally, move them one level up in directory structure everytime before pushing to remote. 

    alias build_blog='bundle exec jekyll build; cp -r _site/tags/ tags/'


### Acknowledgments: ###
* Layout for this blog is based on Eric's excellent tutorial. For details, visit his [github page](http://erjjones.github.io/)
* Thanks to [Charlie Park](http://charliepark.org/jekyll-with-plugins/) 's tutorial on jekyll with plugins.