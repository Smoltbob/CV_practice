# Logging System
After my second year of university, I was working at Pfeiffer-Vaccum for a software engineering internship.
It's a company that manufactures industrial grade pumps for research and high-end manufacturing (solar panels, screens).
I was working in the process department, where the team is in charge of supervising the production in the factory lines. So they were working in things like factory floor layouts, automation and supervision.
The task I was hired to solve was doing a case study on supervision modules that would allow us to gather data on machines more efficiently.
The task I was hired to solve was building a system to perform logging / dashboard.

I didn't have lots of data to do this, so I started to look into what was the current solution, and I tried to think of what they would like to have. So my main requirements were:
- serve relevant data (need feedback there)
- make it convenient (email, table)
- make it quick to visualize (using colors)
 
Then I wrote an early prototype and got some outputs. 
I asked my manager who would be the key users / customers of this system, then I showed them my work and asked for some early feedback face to face. 
They liked my approach and gave me feedback on the way the data was being displayed. 
That allowed me to eventually finish my work according to these updated requirements. 

As a result, I gave them a system that gathers relevant data and sends it as an email every morning. So instead of logging to a separate platform, they would have this email summary sent directly and they would save these 5 to 10 minutes every morning.

## Customer obsession
At the end of this internship, my supervisor invited to a meeting to give me feedback on my work.
He told me he was surprised by how quickly I solved his tasks and that it was great.
I also told me that I should be more assertive, in a way.
At this time, I was very shy, and for instance if I wanted to ask him a question I would just stand near by and wait for him to notice me, because I didn't want to bother him. 
I know that sounds really terrible.
And also, I wasn't very integrated in the team.
At this time, that was the most important advice I recieved. 
I've definitely changed that in my way of working and quickly grew more confident.

## Dive Deep
During this project I noticed some of the data reported was wrong. -> find rogue modules

## Bias for action
I worked on the logging on my own intent.
I let my code for the logging run on the prod server wihtout asking my manager.

## Insist on the highest standards
Even though the current system for logging data was working well, I thought I could improve it.

## Modbus modules
Free and open, developed by Schneider.
They work as master/slave and can give² 1 bit (coil) / 16 bit (register) information in a loop.


# Paper 1
I'm doing my master project half in an academic setting with my lab at university and half with a company based in Toronto called Arcturus Networks. The way it works it that the company gave requirements and I shaped them into a broader question I can solve during my master. Then every month, we have meetings in which I share relevant results and papers, ideas with them.
The main, broad goal of the project is to allow person search, for security and video surveillance applications. 
This can be devided into two main parts:
- Person descritpion
- Person re-identification (to match descriptions)

Focusing on that first part, person descritpion, I wanted to use colors as our main identifier.
I tried to think about how someone would use this system. 
Imagine someone is mugged in the street, or is a witness of a crime.
These things go very fast, and colors are very salient features that we remember easier.

I found that current color models were unsatisfactory, as they had a limited vocabulary size. 
That would mean that we'd have to restrict the vocabulary of the users, and especially if they were witnesses or victims, it's important to let them express themselves as freely as possible.

The only solutions that had a bigger vocabulary were based on complex sets of rules for naming, but I also wanted this model to be simple and fast so that it can run in real time. 

Then I remember having read a comics on XKCD where Randall Munroe, the author, had set up a survey where he asked his reader to name any colors of the RGB spectrum. 
He then released a database of about 3 million named color points.
That was perfect for my problem.
I could train a decision tree, that is a model with very fast computation time, to classify colors.

My model reached state of the art performance (??%) and competes with solutions that require neural networks and that are much more costlier to use, and less general.

## Dive deep
In order to solve this problem, I used a big dataset of color names. 
As I explained in my paper, I believe that using data was the most relevant solution here, as it was encompasing all of our use cases.
Instead of using "perfect" mathematical models, we had data that was representative of all of our customers.

# Live demo
Right as I was starting my Master project, I decided to develop a model for classifying colors in images very precisely. I decided to use a novel data source that hadn't been used before and built my model on that. It allowed me to have a very efficient system that I can use to classify colors in real time.

Once I had this prototype, I wanted to present it to the company that had requested it. So I was meant to talk about it during our next meeting, and probably write a small report for them as well.
But I thought it would be nicer and more convenient for them if I gave them a more visual product.
This way, they can experiment with it and quickly get a feel for it and make decisions.
That would also allow me to give this nice "surprise!" effect to both my supervisor and them.
However I had no idea how to do that.
I learned about Dash (TODO review Dash) and  how to make a live demo and serve it on Heroku (TODO why ? how).
We can display it on a browser, and it has an interactive view of the dataset I  had built, as well as a field to query colors.
That makes it possible to judge wether or not my system is appropriate for them in less than 5 minutes.

During our meeting, they told me they loved it and asked me if it was ok to show it to their clients.

# SERI
Last december, I had just finished my first project and I could have decided I was done with it.
My professor recieved an invitation to go and talk about his research at a convention called SERI.
It gathers relevant researchers from big universities in Montreal, as well as city representatives, like the mayor, and industries for exchanging ideas.

Students are not meant to be there.
However my professor kindly asked me if I wanted to go present here, and made it a condition for him coming.
This was accepted, and I prepared some material as well as the live demo I had built previously.

As a result, I had a great experience interacting with people.
It allowed me to see what was the kind of questions and interests that people outside of my field had.
It was also my first time getting interview on the local TV, I wouldn't say it went great because I wasn't expecting that to happen lol.

# Giving a presentation
I knew that my communication skills weren't as good as I'd like them to be.
It still is one of my weaknesses right now.
One semester ago I register for a course, that in the end involved talking about your project.

# Fractal project
When learning C I had a small project to work on: generated a square binary image of a fractal.
That was my project and I could work on it as much as I wanted.
I love fractals so I tried to imagine multiple features that my users may want.

I made so many improvements to my generator by adding many features that everyone would enjoy on a fractal generator:
- custom aspect ratio and resolution
- colors and smooth colors
- custom color palettes
- custom equations
- parallelizing

All of these requirements made me go so much farther than the goal for the class.

In fact recently I wanted to discover Rust so I wrote a parallel fractal generator, you can see it on my github.


# Battleship game
For a software engineering project, I had to build a battleship game with a peer. I quickly started to lead this project because my pair, while he was working well, wasn't very motivated so I had to push him a bit.

As part of the course our first step was gathering requirements.
Using a small survey we asked our family and friends.
Then we wrote them down and sent to the professors so that they could judge if it would be reasonable project.

Our final requirements were:
- the school asked us to have the computer place boats randomly, and have the player try to sink them.
- so.. you couldn't lose. We thought it'd be nice to have a timer so that we could race against time at least.
- it was a terminal game. So having some colors and text animations would make it look more polished
- if we have time, adding an ai to play against would be great

Through the project, I let friends sit at my computer and just try to break the game. They found a lot of bugs for me this way.

In the end, we finished early and I was a bit disapointed by this game, and since the begining I wanted to make it more exiting, so I thought we could implement an AI to play against, and that would be a proper exciting game. Sadly I thought we didn't have time to build an AI. So a great compromise was to extend our work and allow for a second player to place ships and play. Then that's something two people can play, it's was a much better project to show off.

# QR code
Two years ago I was doing an internship at Creaform. It's a company based in Quebec that has a research and development facility in France. They develop tools for photogrametry. This his very high precision measurements in 3D space with no contacts. Their customers are professionals and industry, like architects or car manufacturers.
Because these tools are very high precision, they require to be calibrated before use with special carbon-fiber rods that have been measured, identified and certified by an indenpendant organism.

When I joined the internship, I knew that the current work would be about working on this calibration process.

### Customers, invent and simplify
One of my colleagues suggested to embed information from these rods such that it would be more convenient for users to calibrate the machines.
This would be both more convenient and also avoid typing errors. 
I thought it would be great to have them as a QR code that could be scanned using the photogrametry sensor themselves, this way we don't need smartphones.
To do all of this I didn't have access to feedback from customers so I put myself in their place and imagined what I would like.
The priority should be reliability, as we don't want measures to be incorect.
So I chose to generate QR code with a high redundancy.
My supervisor also suggested using a special reflective surface, that made detection easier, and had them printed.

I went in the testing room to gather a dataset of QR code images using the sensors.
I used this dataset as my feedback, aiming to get as many positives as possible.

### Have backbone, invent and simplify
As far as techniques were involved, I suggested trying out machine learning using a simple convolutional neural network. 
I think that it would have given us some great results and that it was worth trying.
I looked at whether or not it would be possible to do it right now and in fact they had bought a licence for Intel OpenVX (?) that supports machine learning abilities.
Then I looked if some similar projects had been done, mostly looking at shape detection, and it's even a task so simple that it's considered a toy example.
I told about this to my supervisor.
I had a very traditional approach to computer vision and he raised concerns that this solution could fail.
That's an argument I couldn't really counter, as we wanted the highest standard in terms of reliability.


### Invent and simplify, Are right a lot
Instead of using in-house, OpenCV.
I thought it would be more efficient.
My supervisor wasn't convinced about this idea, because of licensing issues.
I dealt with these two points using benchmarks and I dug deep to see that they were already using Intel OpenVINO.



# Mineral pedestal
A friend of mine buys and sells high end minerals for a living.
These are very expensive pieces worth thousands.

He's always trying to bring new ideas into his field, and we often end up brainstorming together.
He was telling me that he was thinking it would be really cool to give his buyers along with the mineral they buy, a pedestal that would be perfectly shaped for that piece.
So I started thinking that by somehow scanning the bottom of the piece I could get a mold and then 3D print it.

But first that's expensive and second that's not often feasible as I would have to lay the mineral upside down, and they are so fragile that it's not even thinkable.
Then I realized that I don't need a 3D scan, and in fact instead of thinking about hollowing a shape I could think about filling space. And instead of a continuous shape I could think of discrete points.
How many points to we need to hold an object in space ? 3, and we could get these 3 points using only two pictures: ne along the x axis and one along the y axis (along with a depth measurement).
So I came from an unfeaseable 3D scanning solution to a much more reasonable picture solution.

I told him about this and we'll continue to define this better.

# Compiler


In my team there was a guy who was not very cooperative.
He was very smart, just like every one my team, but he had troubles communicating and he wanted to do most things his way and on his own.
I didn't want to let him take control of the direction of the project because that was my role and I wanted to have everyone participate in these decisions. But I didn't want to micromanage him either.
We weren't confrontational either.
So when assigning roles I asked him if he'd like to work on optimizations, because I knew he's very good in math and loves it.
So he liked this role, and that was also one where he could kind of do whatever he wanted because that was his field and he had authority there.
This worked well for most of the project.
Then at the last day, before the deadline, we all met and pushed our last commit and agreed to not touch at anything, as we were satisfied with the project.
But in the evening, I saw that he was still working and pushing stuff, and I couldn't contact him, so I revoked his rights to the repo.

I don't like that I had to do this, but that was my responsability and the whole team was going to sleep excpecting to present the following day on a state of project we had agreed on.

# Github Project
There is an institute in the UK called Forensic Architecture. They are non-profit and aim to use open access data to highlight and give proof of human rights abuses. I discovered this agency while I was following the Syrian civil war, and they had released a study on a gas attack on Douma in 2018, during on of the last pushes of the Russian army.

I saw that they have a public discord as well as a github repository, so I asked how I can help.
They told me they are looking to add new analyses to their tool.

Using my experience in computer vision, I adapted models developed by other researchers to FA's framework.

Now we can detect protests, violence and fires.


## Bias for action
Fixing build issues and co on my own.
The project lead wasn't very responsive.

# Hackathon
TODO use "I"
I joined a hackathon with two of my friends. 
The goal of this hackathon was to write an ai for playing a modified game of snake, that plays against 4 players.

## Bias for action
We had to deal with incomplete / lack of data, and make decisions quickly.
We had a time limit to act, and that hackathon wasn't very professionaly managed.
Our requirements as well as the rules of the game and the API we'd be using weren't well defined, and the contest was late to open.
As we were waiting for the API to be unlocked, I started to think about high-level ideas and strategies.
Should I go with a defensive or offensive approach ?
I chose defensive, as it would be faster to implement.


### Invent and simplify
To solve this project, we had to come up with our own solution.
We decide to go for defense over offence.
We started with a simple baseline, on which we expanded.

# Drone Project

# JPEG Project
I was working on a software engineering project.
We were three working on it and every one had an equal responsability.
The goal was to write a pipeline for decoding JPEG images and save them to an uncompressed file format.
So we had to handle data loading and the multiple steps of decompression. TODO read on JPEG.

At some 

# Heart rate monitor

# VHDL speedometer

# AECSP

# Learning Arabic

# Helping newcomers by writing a wiki page
At my work place there are about 70% percent phd students and 30% grad students. Virtually all of them have academic backgrounds and not engineering like I do, so I often saw them struggling to do "basic" tasks. 
On top of that, every trimester, new colleagues join us.
Rollover is between 2 and 6 years.

When I joined the lab, I realized there was no real way of communicating and storing information for everyone. 
They only used one to one communication through email.
That struck me as an issue as that pretty much prevents you from sharing knowledge with more than one person at a time, and thus you can have any kind of multiplication of knowledge.

I introduced using Slack as a communication tool.
That made asking questions easier, but also setting up meetings and sharing information, useful papers. 
Newcomers have instant access to all that information.
And in particular, I set up a Slack channel as a wiki page, meant for all of us to share useful tricks, command line tools, how to solve these common and annoying problems that we all face.
So now, when I learn something new, I can spread this knowledge to a dozen teammates instantly.

At first, my professor wasn't convinced of the usefulness of Slack, but he agreed to let me introduce it as long as it didn't add him any more work.
Nowadays he agrees that it's very useful.
This has proven very useful during the pandemic, as I had already wrote a guide on working remotely.


# Helping Hadrien
During my first year of studying at university the son of my landlords was working on his business buying and reselling high end minerals to museums and collectors.

I practice photography for ten years now, so he asked me for help taking pictures of his minerals. At first, I took the product shots myself for him.
Then I taught him photography 101.

As a result, he had a nice website and since then he's kept himself up to date. Now he's looking at photogrametry and 3D scanning.

# Help friends learn French

# Paper 2
During my grad studies I worked on a project that aimed to output which colors were present in relevant parts of an image. 
This typically requires lots of labelled data for training.
Therefore this requires users to pay more to gather and label data, possibly severtal times per location or time of the year, and to use more expensive hardware.

I wanted to avoid that, so I thought I could reuse instead a neural network trained on a simpler dataset, and use explanation methods.

I measured my results using two different metrics: intersection over union and color prediction over semantic parts.

## Dive deep
I order to solve this problem, I decided to reuse a neural network that was trained for another simpler task, and to look at its gradients as it processes images.
This involved an in-depth comparison of algorithms, as well as testing, because in my situation, it was very easy to fall into visual confirmation bias (in fact this happened at first).
In order to know if I was doing the right thing, I set up test benches and defined metrics as proxies, that would allow me to judge if my methods had a positive influence on the end result while being as little visual as possible.

## Bias for Action
Early in the project, I knew I wanted to use explanation methods.
However, there are many of them with a lot of litterature and use cases.
I decided to clone a collection of implementation of Github and directly experiment with them.
I build an early prototype and set up benchmarks to get some data and know how this new approach compares to my last one.
This way, if I had terrible results from the start, I may not want to continue.
However, I had encouraging results, so I put my prototype aside and continued reading.

## Deliver results
I got some promising results in this project.
Eventually, I reached a plateau, and while I knew I could squeeze some single digit percent increases by fine tuning, I was trying to get some more significant improvements and also some more significant experiments, as tweaking hyperparameters does not bring a lot of value to my work for my lab.
I was stuck here, so during our weekly lab meeting, I shared my hinsights and my concerns.
Most of my teammates are PhD students, and have great experience.
One of them suggested me to try a completely different loss function, that would basically make the problem into a different type of optimisation problem.
I had considered this, but discarded this idea as being too simple, naive and not elegant enough.
But this time I folowed the adviced and obtained some interesting results.
This is very recent so this is only visual, but I'm hopeful this is the direction I will move to.

Out of this, I learned to never discard ideas for being "too naive", and in fact that's something that already helps me when solving algorithmic questions.

## Think big
To solve this goal of using less data, I decided to use explanation methods.
This is a new type of methods that is not commonly used to solve my problem, although intuitively it made sense to me.
I took a risk here as it was not a commonly known way of solving my problem.
In order to reduce the time potentially lost if that didn't work out, I planned to build a prototype ASAP using open source implementations of recent papers and apply them to my pipeline.
I defined relevent metrics to my usecase, in order to have some proper data to make my decisions, and not get tricked by confirmation bias.
When I saw an improvement in my metrics, I decided to move forward with my idea.

# Database project
