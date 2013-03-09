Heroku is a PAAS (Platform-as-a-service) that has set a standard for
web application deployment and hosting.

Part of the deployment process uses a open source standard called "buildpacks".

Buildpacks have 3 steps in which they determine how a piece of code
being deployed should be treated.

1. Detect: Detects if the application will work with the buildpack.
2. Compile: Builds the necessary dependencies for the application.
3. Release: Releases the application as "complete" in a standalone package.

I maintain several buildpacks.

- [heroku-buildpack-gostatic](https://github.com/pearkes/heroku-buildpack-gostatic)
- [heroku-buildpack-static](https://github.com/pearkes/heroku-buildpack-static)
- [heroku-buildpack-pelican](https://github.com/pearkes/heroku-buildpack-pelican)
- More about [Heroku Buildpacks]()
- A [post](http://localhost:4000/post/gostatic-buildpack-for-heroku/) about the gostatic buildpack
