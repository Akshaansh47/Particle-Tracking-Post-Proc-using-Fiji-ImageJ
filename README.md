# Particle-Tracking-Post-Proc-using-Fiji-ImageJ

**Overview**

This code enables the easy extraction and analysis of data from Particle Tracking results (ideally saved as CSV files). The intended software to be used is the Fiji ImageJ software that makes use of the TrackMate plugin to perform particle tracking on a sample that is being observed.

**About**

Particle tracking is a process that helps us understand the effects of a force or displacement at a specific point on a sample. The main application is in large lattice structures, wherein a number of vertices are in motion at the same time and capturing each one is of the essence. The results will show us trajectories, displacements and scatter plots of the various states within the experiment, whether across frames or across particles.

**Requirements**

Ensure that your data is available in .csv format and that you have ordered all your data by frame (using the Filter Sort tool on Google Sheets or Microsoft Excel). The desired order is of every particle in ascending order within each frame and every frame in ascending order overall.

**Functionality**

This project provides the following functionalities:
1. A scatter plot to show particle positions at any frame throughout the movie.
2. X,Y-locations of each particle as a function of time.
3. Displacements (net, using sqrt(x^2 + y^2)) of each particle as a function of time.
4. X-Y trajectories of each particle, which is helpful to see the start and end positions of any particle(s).
5. Trajectories of all particles over time.
