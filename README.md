## Table of contents

- 1. Introduction
- 2. MyDRTV
   - 2.1 Criteria
   - 2.2 Selection
- 3. Toxic Chemical Industrie A/S
   - 3.1 Criteria
   - 3.2 Selection
- 4. HolidayHouse
   - 4.1 Criteria
   - 4.2 Technology stack selection process
      - 4.2.1 Expert analysis
      - 4.2.2 Analytical hierarchy process
            - 4.2.2.1 Frontend
            - 4.2.2.2 Database
            - 4.2.2.3 Backend
      - 4.2.3 Supporting technologies
         - 4.2.3.1 IDE
         - 4.2.3.2 Version control
      - 4.2.4 Selection summary
   - 4.3 Development planning
      - 4.3.1 Prototype scope definition
         - 4.3.1.1 User story
      - 4.3.2 Coding standards/conventions
      - 4.3.3 Git strategy
   - 4.4 Development process
      - 4.4.1 Switching database from SQLite to MySQL
      - 4.4.2 Search functionality
      - 4.4.3 Design prototype
      - 4.4.4 ER diagram
   - 4.5 Reflection
      - 4.5.1 General technologies and methods
      - 4.5.2 Language, framework and database
   - 4.6 Conclusion
- 5. Source list
- 6. Appendix
   - 6.1 Analytical hierarchy process
   - 6.2 Mockup
   - 6.3 ER diagram


## 1. Introduction

For this project we were given three scenarios to consider for our main case. We chose the
HolidayHouse scenario. We made the decision unanimously during one of our first meetings. In
this report we documented our analysis of the criterias for each of the three scenarios and
created a technology stack specified and considered out of these criteria. The report goes more
in depth about the selected case; the HolidayHouse. We explain why we chose the specific
analytical methods and how they led to our recommendations. We conducted research
confirming and supporting our statements and conclusions. After defining a technology stack for
our case project, we developed a prototype for it. This demonstrates our development planning,
in which we define our scope and general strategy.


## 2. MyDRTV

DRTV wants us to develop a new web application called MyDRTV. The goal of the application is
to promote Danish television shows and films globally. The solution requires a rating system.
Next to this DR wants us to focus on user retention by implementing targeted recommendations
along with a platform for social interaction between users. To present DR’s library of TV shows
and films they made demands for a search engine with filters.

### 2.1 Criteria

We have analyzed and interpreted the system criteria out of the scenario’s functional
requirements. It is stressed that availability is a main priority of the system. Because of this, the
considerations concerning the database provider, hosting service along with various potential
fail-safe systems in place, providing backup and alternative live versions.

Since the system’s target is to reach out to a global audience and it needs to be able to handle
a lot of requests, scalability is also a consideration to keep acceptable speeds. This is of course
an important factor, concerning optimizing the data flow to ensure user satisfaction.

We have considered that the application would have to be hosted on multiple servers around
the world, to comply with availability and optimize the general user experience. This would
require backend functionality that would synchronize the data changes and interactions so the
users have a live connection to each other.

DRTV has a huge amount of data to present if they really wanted to. The data is also going to
be mainly video type files. This means the application needs to be able to handle large amounts
of data and since the user base is targeted globally we expect a lot of users. Combining these
facts we need to highlight the importance of storage capacity and efficient delivery to the user
along with potentially heavy querying through various filters.

Internal social networking in the form of user communication, interaction, rating system etc. will
imply that the application has to properly handle personal data. GDPR compliance is obviously
a requirement.

Our application also needs to be able to collect the user’s choices and movie taste. Tracking is
necessary to get the system to respond with targeted recommendations and make the user
continue to be a consumer of our product.


### 2.2 Selection

Based on the above criteria assessment, determining that availability and scalability are the
most important factors and leaning on the cap theorem model, we have come to the conclusion,
suggesting a database like Apache Cassandra. Cassandra stands out in fault tolerance by
having replication across multiple servers or even datacenters. This is also the choice of Netflix
which is a similar service.^1

For the programming languages we suggest to take a microservice based approach. This
makes the app lightweight in the frontend and the backend versatile. The backend could be
written in a Python framework such as Flask and the frontend in a Node.js based framework.
This combination could work well as it is very simple to write API’s in python.


## 3. Toxic Chemical Industrie A/S

Toxic Chemical Industrie A/S wants to have a web application to manage processes for storage
of chemicals at various depots in the EU. Since they are storing toxic chemicals, the process
needs to comply with special laws. Because of this, the records must be available for external
inspections. They have asked us to help develop a software system that helps with the
compliance with the legal regulations. There are also storage regulations we have to consider.

### 3.1 Criteria

This is a special case when we look at the importance of data integrity. Storage is regulated by
safety laws and there are specific laws on what type of chemicals that are being stored. This
also requires some extra thought and consideration towards logging and validation reliability to
help force human or system level mistakes not to occur or even be possible. In the case of a
fault occurrence, this would warrant a very detailed record and security measures to diminish
potential integrity damage.

We thought about adding the aspect of users being able to report failures or alerts on when
something is going wrong and the system should then react to it. This would supply more safety
for the workers. At the same time the company only wants a prototype. So trying to add more
would maybe be out of the scope. We think of this project as a Proof of Concept. They want to
know if this would be a good investment into the management’s compliance team to ensure the
complex regulations are adhered to.

### 3.2 Selection

Our choice for the database is Oracle Server. The reason for this is because Oracle Server has
both audit tables and different mechanisms that ensure the data consistency.^2 We value this for
the reason that Toxic Chemical Industry needs to be able to verify every change. Also this
database gives a lot of controls on how the transactions are performed.^3

On choosing a programming language we would recommend it to be strongly typed. With
strongly typed languages variable types have to be explicitly defined and cannot be mixed. This
helps with preventing the possibility of producing defects in your final product and leads us to
recommending fx C# with ASP.NET MVC for developing the product.


## 4. HolidayHouse

We have been tasked with building a new web app for HolidayHouse. The company has a huge
amount of pictures from house owners that rent out their second house, through their portal.
The app has the purpose of helping to make reservations.

### 4.1 Criteria

HolidayHouse currently has 5 million pictures that need to be shown into the new website. This
requires a certain level of scalability of the file storage and database. Also it is a good idea to
think about the hosting setup, to reduce cost.

The visitor of the website should be able filter on many different accessories of the houses.
These are for example whether it has a pool, sauna, but also location, etc.

We should be able to securely accommodate sensitive user data. The app should integrate a
secure transaction provider. Outside of internal data security there is also a concern considering
external validation of the legitimacy of the landlord’s product and the potential for scams.

We should look at opportunities for making the UI better or special in terms of design and
functionality. The user should feel attracted to revisit the website and needs to feel in control.

Ideally constant availability and minimizing downtime, maintenance etc. as much as possible.

The final product should have a public API, in order to integrate with third parties.


### 4.2 Technology stack selection process

After some preliminary analysis we determined the frontend to be the most important part of the
solution for the company. The product should be heavily focused on delivering a crisp and
optimized UI and UX to pertain to user satisfaction and credibility.

While we needed to also consider the weight of user influx and its marks on system
performance. - We knew from our previous research that both a NoSQL and Relational
database could potentially be able to handle the expected data traffic of this project.

For the backend we consider it mainly important that it supports the frontend with getting the
right data and handling the logic. Regardless of choice here, it should be able to meet the
performance and functional requirements of the application just fine.

We consider team experience for the frontend technology not to be a particularly crucial factor.
From our experience it is fairly easy to learn a new frontend framework compared to learning a
new backend language or database language. However in terms of our project development
scenario with the given time and resources, we think it is important to stay close to what we
already know, as a knowledge resource and therefore weigh it higher than in a professional
production process.

#### 4.2.1 Expert analysis

_“server side rendering - i would go for that if you use a CMS that will give you a lot of things out
of the box, fast developing, as it comes with a lot of things. In that case if you don’t want to
modify much and just add functionality + markup + styling, it’s a good solution as it’s fast. But
you have to follow the structure it gives you._

_client side - it gives you a lot of flexibility. You can basically do whatever you want, and the
structure could be whatever you want. You can modify it in every way possible. You are the
architect in that case. I would recommend it for very custom solutions, It's much easier for the
frontend. Overall development time is slower than client side - but it’s much more flexible and
you can use whatever tool you want”_

- A colleague of Marijn, whose name is known by the authors of this document.


#### 4.2.2 Analytical hierarchy process
![Analytical hierarchy process](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image10.png)

We decided to make an Analytical Hierarchy Process model (AHP) in order to get an overview
on how we weigh the criteria for the frontend, backend and database. This will be a guide to our
final selection.

Both the choices for Django and MySQL seemed obvious to us for this project after we
constructed the analytical model. The frontend was however still in debate, as the choices are
very close to each other. In an ideal scenario we would definitely recommend to use a
framework that renders server side. Svelte does this by default and React has good options for
doing so. Also Django renders it’s templates on the server side. We go more deeply into the
choices for backend, frontend and the database on the following sub-chapters.


###### 4.2.2.1 Frontend
![Analytical hierarchy process frontend](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image1.png)


We have put emphasis on this part and find the
support for single page applications quite
important, since we believe this improves the
user experience by a substantial amount.

The support of the frontend framework is also
considered important. Working with or using an
obsolete framework is not great. And since
frontend frameworks come and go more often
and other programming languages. Like in the
case of AngularJS^4 and many others. Therefore
we put a lot of weight on the importance of the
support.

##### Svelte

**Server side rendering:** ​ 10
Since svelte is made for server side rendering, it
is only reasonable to give a score of 10.
Because it’s made for this type of rendering
there are no problems or work around needed,
nor slowing down of the service.

**Maintenance/updates:** ​ 4
Due to being relatively new and lacking industry
adoption, Svelte does not have a huge resource
pool to support a comparatively high level of maintenance and updates. On the other side it is
open source based and is in a growing state within the Node.js community.

**Single-page app capabilities:** ​ 8
If you develop a frontend UI with svelte as standalone then Svelte is built for developing
single-page applications. But there are packages and frameworks that support implementing
routes with the normal http request cycle. But because Svelte is built for single-page
applications we have decided to score it high.

**Team experience:** ​ 4.
The majority of our team has some experience with Svelte, but the score is dragged down
compared to vanilla JavaScript, where we all of us have some level of knowledge.



##### React

**Server side rendering:** ​ 8
React handles server side rendering quite well. But compared to Svelte where it was made for
this type of rendering, React is less optimal. Getting it to work might not be as intuitive as other
frameworks.

**Maintenance/updates:** ​ 7
Being produced by Facebook along with open source integration and its huge popularity means
that React has a solid resource foundation for maintenance and updates.

**Single-page app capabilities:** ​ 9
React is very good at client site functionality and creating dynamic pages. It is rendered
server-side and with React Router you can develop “multi page” single-page websites.

**Team experience:** ​ 3.
The majority of our team has close to no experience in React. So the score is significantly lower
than the other options in our AHP diagram.

##### Vanilla JavaScript

**Server side rendering:** ​ 6
JavaScript is a just-in-time compiled programming language^5 , it was made more for client side
rendering. Although JavaScript is the base for many other frameworks, and libraries that could
make it even better at server side rendering. We feel like vanilla JavaScript just isn’t as good as
other frameworks like Svelte, that was made with that purpose.

**Maintenance/updates:** ​ 10
JavaScript is the baseline technology that other frameworks make use of. This makes
JavaScript very popular and an established language and essential technology for web
applications in general. Hence majorly supported in terms of maintenance along with updates to
keep the language refined and organically evolving to stay relevant and cutting edge.

Both react and svelte are frameworks which means they are subject to a volatile lifespan, strong
fluctuations in popularity and will always be subject to rise or fall.

**Single-page app capabilities:** ​ 6
JavaScript is not made specifically with single-page app capabilities in mind. It loses some
points in comparison to others, although JavaScript based framework, they were made with
these things in mind. Our score is based on the fact that it’s possible to use vanilla JS to create
a single page application, however doing so with a framework would save a lot of time.


**Team experience:** ​ 6.
We have the most overall experience with vanilla JS, also it is widely used and adopted.
JavaScript has become somewhat of a standard when it comes to the development of
interactive website and web applications.

##### Conclusion

The result from the AHP show to favor vanilla JavaScript over the frameworks. This is favorable
given the team experience with both the frameworks and vanilla JavaScript and the limited time
for the development of the prototype. Vanilla JavaScript would be easy, flexible and fast to use it
doing the prototype development so we have chosen to use it going forward in the development.
But in case of making a finished product, using something made for server side rendering might
have been a better choice. Using server side rendering does require good server hardware, but
it makes for a consistent user experience, since you are not reliant on the client.


###### 4.2.2.2 Database
![Analytical hierarchy process database](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image3.png)


##### Initial analysis

The given problem description states that the current stack is struggling to cope with an
increase in usage of the service and the requirement for heavy load traffic including
approximately 5 million picture’s reference storage and queries along with any other
conceivable user interaction.

Naturally this means the choice of database and especially its model type becomes significant
for performance and stability. We determined that relational and document models were the
relevant options for a project of this type whereas something like key-value stores or graph
based would be polarised towards systems that address and offer solutions to issues outside of
the scope of this product such as IOT, pattern/behaviour, cache-only etc. - Something we have
covered more in detail in our previous database analysis report.^6

When considering the scenario of high volume user interaction traffic, every little logic operation
that interacts with the database through the request/response cycle will add up and put a lot of
pressure on the database and affect its query times. While a relational model with joined tables
and potential additional operations such as triggers, transactions etc. will result in slower
queries it also enables transactional integrity and extensive records, which could both be very
relevant for this project depending on the functional requirements (currency transfer, logging,
cascading operations etc.). On the other hand a document based model would result in faster
queries and better scalability prospects but sacrifice normalization and data integrity which
would mean requiring more storage space and limiting possible functionalities.

From this analysis and leaning on our previous database research report, we have determined a
set of numbers and candidate choices; MySQL, MongoDB and SQLite for our AHP.

##### Consistency

Consistency is one of the lower valued criterias of our solution. While it is preferred to keep data
as consistent as possible it is not a critically essential consideration since we are not dealing
with transactional or other data that requires absolute consistency. Money transfer for bookings
will be handled by 3rd party tools. One example of which to consider the value of the
consistency of the booking system. It will need to deliver accurate available and occupied dates
to all clients.

MySQL scores well in consistency because it can enforce constraints whereas in mongo for
instance you need to use transactions to make sure that this is done the right way. Because
SQLite does not support triggers we value the consistency lower due to the fact that it is not
possible to make audit trails, furthermore it is not possible to make stored procedures, this also
impacts the data consistency as functions are not generalised.


##### Team experience

This is the criteria we rated highest for the database. This is entirely weighted towards this
project scenario and what is realistic given our time constraint. A database system particularly
can be very time consuming to learn and produce a lot of issues setting it up on different OS
configurations.

The general experience level of the team strongly favours MySQL, it is the platform we primarily
have been working with earlier during our database course, so it is the most familiar by a
marginal stretch.

##### Availability

The system should be able to function with partial node failure, while complete system failure is
a high priority to avoid, a large portion of the data involved will not be critical to keep the app
functioning. It will be in the static content category (basic displayed information).
That being said, there are options for securing availability despite the database choice, such as
employing multiple data storages, caching, backups etc.

By default MongoDB has a lower availability while the relational databases are high. It is worth
noting though that, with utilizing replication^7 this can be increased significantly.

##### Support

When talking about support, we have categorized and distinguished between:

- The manufacturers support in terms of updates, maintenance, documentation and
    tech-support along with community size and involvement.
- The list of unique or relative functionality the database system offers.

All of our chosen options are well established, big players on the market, so naturally they will
all be rated rather high in the first category and considered to be relatively safe to rely on.

In terms of functionality however, MySQL and the relational model in general tends to provide
more functionality to control the data as it is tailored to enforce consistency whereas NoSQL
databases will be mainly focused on scalability capabilities. SQLite of course is an outlier in the
relational category in this regard since its purpose is to be lightweight.

##### Scalability

Scalability is strongly hinted as a primary objective to solve in the solution, with it’s
aforementioned 5 million picture uploads per month along with other queries.
This of course points towards a NoSQL solution capable of high scalability. While scalability is a
consideration to keep in mind, this system’s expected query traffic does not warrant the “big data” kind of magnitude that a NoSQL system caters to. A relational model should be plenty
capable to support the amount of queries in question.

##### Conclusion

The result from the AHP points towards using MySQL, while this of course is only a guidance
measure, it aligns with the group’s assessment. It offers a good balance between data integrity,
functionality implementation freedom and reasonable performance as long as the system
doesn’t grow into relative proportions of “big data”. Additionally and importantly, our team has
the most collective experience with this system. - Within the scope and circumstances of this
project, the learning curve of adjusting to an alternative system would consume a lot of valuable
time resources.

In a real world production scenario the most ideal solution would likely consist of a split solution
where both a relational database and a NoSQL type database would be utilized for optimal
performance and data quality. This of course would mean a much more sophisticated system
would need to be designed and resource cost would increase. Given the project description it
would likely be a realistic approach. Also adding a caching system for images with redis,
memcached shouldn’t be taken a lot of time in a Docker or UNIX environment.


###### 4.2.2.3 Backend
![Analytical hierarchy process](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image4.png)

Backend got less points than frontend because we think that the functionality required by the
product could easily be made in almost any backend language and framework. The final choice
is mostly going to be defined by our team experience because of our timetable. Therefore we
only included languages and frameworks that we have used before. The support for the
backend is also important. This helps provide more software quality assurance and persistent
package reliability.

For the backend we analysed our options primarily from a security perspective.

Analysing the security of a framework or language comes with a lot of things that could be put
into consideration. For our selector process we have looked at just a few indicators to come with


a score. These include the amount and types of CVE’s^8 that have been published. Next to this
we have looked into how frequently updates security are made available. The last thing we take
into consideration are third party packages.

Node.js projects often heavily rely on packages published on NPM. The issue with this is that
packages are barely scanned for security flaws and developers are used to integrate these
packages without analysing the source code and vendor. For many developers the problem with
this became evident lately when in 2018 Bleepingcomputer published an article about how a
Backdoor was hidden inside a very popular NPM package^9. NPM actively removes malicious
packages but this often happens after damage has been made.
Another problem with this model is that whenever a NPM account gets compromised and the
package gets updated this will be quickly diffused to a lot of applications. In 2016 a developer
broke thousands of projects by writing as few as 11 lines of JavaScript in his commit to a
dependency of Node.js.^10 The likelihood of such an attack became much higher after 2017 it
was revealed that 52% of all npm packages could have been hijacked due to poor credentials^11.
This issue was resolved by resetting all passwords of users with weak security standards, but
this still proves some of the security weakness of the trust model.
The amount of CVE’s on Node.js at the moment of writing is lower than the other candidates but
we consider the security of a solution with Node.js and this is likely to include many
dependencies.

For PHP there have been over 600 CVE’s reported of which 19% was a possibility to remotely
execute code.^12 This indicates a poor security standard when the core of the language was
originally developed. In PHP's defense, many of the issues are resolved, although not always
deployed as quickly as one would hope. Unlike Node.js-, PHP-projects don’t rely on a big set of
packages, instead mostly a few standard extensions to the language. The extensions can be
installed through PECL or PEAR, both are part of the PHP Group project and applications are
manually approved^13.

Django’s CVE’s are mostly about XSS- and CSRF-protection bypasses, while this is something
you really do not want to have, it is something that many other frameworks do not offer
protection for out of the box. In 2019, someone also discovered an SQL injection possibility in


Django 1.11x, this version is very outdated and should not be used^14. Django 1 is fundamentally
very different from the versions from and above 2. Django offers all sorts of security features
such as seraliazing, session and authentication protocols and out of the box protection for
common security problems such as XSS and CSRF.

When it comes to packages, Python is much like Node.js, Pythons Package Index; PyPi is
similar in a way to NPM because anyone is able to publish packages to it. This also went wrong
in 2018 when 12 packages with misspelled names i.e.djago or djanga were removed because
they contained malicious code which sent data to Chinese IP addresses.^15 In 2019 also 3
packages got removed after almost 20 months when a security firm had discovered the
malware.^16

While these are serious events, we consider Django also on this part a more secure framework
then Node.js. This is because of the amount of malicious packages discovered on NPM.
Moreover Node.js projects use much more dependencies and that also increases the risk. It’s
advisable to install some software checking for insecure packages.

##### Conclusion

If we only look at the score sums then PHP and Django are very close to each other. We could
have chosen either one but our team experience is higher on Django and the research results
on security gave us credible results that Django is the best choice.

#### 4.2.3 Supporting technologies

##### 4.2.3.1 IDE

We researched different IDE’s based on what language and framework we are developing in.
The best IDE recommendations for developing Django projects all mentioned Jetbrains
PyCharm IDE. This IDE has features that compliment Django developing very well. You can
easily create environments, it has a great debugger and you can configure and query your
database from the IDE. Also PyCharm puts the configuration on for example indentation in a
folder so that we can keep this in sync among the team members.


##### 4.2.3.2 Version control

To support remote development and us as a group being able to work on the same project at
the same time we had to implement some kind of version control for an optimal work process
synchronization, we chose to go with the industry standard approach of using git along with
github.

Using git enables a structurally sound and compartmentalized system that offers a lot of control,
damage mitigation tools and insight if utilized correctly. The cost of this however, comes with a
learning curve for the untrained and potentially a considerable amount of re-iterating over
process steps and roll-backing, which can become time consuming. Something we indeed
experienced to a certain degree in our process since not all of our members is seasoned git
users.

#### 4.2.4 Selection summary

The ideal scenario where time and resources would have no relevance we would go for Django,
Vanilla JavaScript and MySQL. But as explained in the previous conclusions we are only going
to develop the prototype within Django’s capability scope and use SQLite as our database.

As for other technologies we are going to use Figma for mockups, Git along with GitHub for
version control and PyCharm as our editor.

### 4.3 Development planning

#### 4.3.1 Prototype scope definition

Because we are working with a strict timetable we decided to narrow down the scope of our
prototype to one specific element of the product. We are going to focus on the customer’s
process of finding and creating a booking. To help document and specify this journey we have
made a User Story to define it. Although choice of frontend is important for the user experience,
we want to focus on the underlying support for the frontend in our prototype since actually
implementing the frontend mostly comes down to a methodic, time consuming process.

##### 4.3.1.1 User story

We created a user story to define what the actor wants and why. After this we defined tasks out
of the story. To the right of the tasks we created a task network to help plan how and what tasks
depend on each other.


**Find and book a holiday house**

**Actor:** ​Customer

As a customer I want to search for a holiday house using filters like location because I want to
create a booking.
![Task network](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image7.png)


**Tasks
1_1**
Wireframe for index.html (view list, search page,
category entries)

**1_2**
Wireframe for property.html (view detail)

**1_3**
Creating ERD model

**1_4**
Creating database models in django

**1_5**
View function and template design of index.html (view
list, search page, category entries)

**1_6**
View function and template design of property.html
(view detail and booking)

#### 4.3.2 Coding standards/conventions

To help provide software quality assurance and consistency in naming and general coding style
we want to document that we followed Python's PEP8 coding style and conventions. Fx variable
naming is in full lowercase with snake case for spacing, class names are Camel cased and
starts with an uppercase letter and class names should also be a noun. Our IDE, PyCharm
helps us to follow these conventions.

#### 4.3.3 Git strategy

We will set it up with one main branch. The procedure for completing a task from our product
backlog will then be as follows.

1. Create a branch out from the main branch named the same as the task number for
    reference.
2. When the task is done then merge the main branch into the task branch and solve any
    merge conflicts.
3. Create a pull request to the main branch.
4. Get it reviewed by another team collaborator. If it is not validated, start over until it is
    accepted.
5. When validated the task branch will be pulled into the main branch as a new “baseline”.


This approach where we implement the requirement of having another developer review the
code before committing it into the main branch adds another layer of software quality
assurance.^17

### 4.4 Development process

In this chapter we describe how we encountered and solved some issues we faced during our
development process.

#### 4.4.1 Switching database from SQLite to MySQL

Our AHP led to MySQL as the prefered database. Configuring Django to use MySQL turned out
to be very easy on our unix distributions, but we did run into issues with setting it up on a
windows machine. We decided on a timeframe to solve the issue and if we were not able to, we
would revert to using SQLite to avoid spending too much time solving this problem. - Since we
were not able to find a solution, we decided to use SQLite for the prototype. SQLite also works
well here since it is natively set up and pre-configured with Django while still deploying the
essential functionality and structure hence saving us development time. Transitioning between
the databases is seamless thanks to Django’s migrations and “model” structure, with just a few
lines in the settings file the database can be configured.

#### 4.4.2 Search functionality

Django has an easy way to make select queries. We utilized this in our search functionality to
search through properties by zip code, city or country in the same query.

#### 4.4.3 Design prototype

In designing the GUI for the frontend we chose to use Figma. A few of our team members have
previously used figma for a recent project, with positive results. The tool is rather intuitive,
simple to use and enables swift graphic modeling in a collaborative real time environment and
even supports interactive functionality integration for a rudimentary prototype.^18

![Designing the prototype](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image8.png)

One thing we did not antecipe was the changes we ended up doing to the ERD under the
development. When making the mockup, we ended up adding additional things to the detail
view and the frontpage that was not originally described in the ERD and therefore not in the
Django models. The mockup resulted in both changes to ERD but also to the Django models.

#### 4.4.4 ER diagram

Our ER diagram does not strictly follow the normal ER conventions regarding documenting the
data types. The reason for this is we found it easier to read and use if we wrote the datatype
names the way Django models define them.

There was one complication. In the Country tabel we wanted to use the database type ‘char’
and not ‘varchar’ for the “country_code” field. Django models do not support this. So it required


some research but we found an easy solution. Django supports custom model field types. The
type name just has to be included in the database data types.^19

![ER diagram](https://raw.githubusercontent.com/ph00lt0/holiday_house/master/documentation/image2.png)


### 4.5 Reflection

In this section we will be reflecting on our choices made to this point and answering the
question: ​ _Did we choose the right methods and technologies?_

#### 4.5.1 General technologies and methods

Let’s start by looking at the IDE PyCharm. It was easy to install and it’s capabilities helped with
the development process as we had hoped.

When we first started using Git, one of our team members had problems that caused some
setbacks. But the git tools and our strategy prevented a total break on the main branch.

One thing we really utilized was having the ERD updated at all times. This way there were no
problems with cross developing with the same data models because everyone knew what the
names were and what it contained. We also started out by creating some test data and adding a
sql dump file to the repository.


#### 4.5.2 Language, framework and database

We think Django was a good choice for developing the prototype. All of us knew the basics and
some more, so we knew how to complete our tasks. No time was lost on learning new
languages and frameworks. Django also makes the database creation, changes and connection
very easy. You define a model and migrate it. Compared to PHP where the database tables are
made with either selfmade queries or via a UI for the database. Then you have to manually write
a connection to the database and define classes that fit the data or work with JSON objects.
Moreover the insert, update, select and delete queries will all have to be made from scratch.

We also got a feeling for the capabilities of Django and how it could benefit the development of

##### the full product. For example Django models have a field type called ​ ImageField ​ that handles all

the image upload factors like storing, validating and referencing in the database.

Overall Django offers a great framework for efficiently building a full stack product that is quickly
up and running, including a lot of very practical tools for supporting or cutting down production
time for common functionalities, validation, security etc. This is something we also felt was
confirmed during development, since the production of the prototype went rather smoothly.


### 4.6 Conclusion

Throughout this project’s analysis and selection of methodologies we have learned a lot about
the importance of early choices when dealing with a new project request. The outcome of the
product is defined by the technology stack and how well you have analyzed the criteria of the
full product's functionality and required capabilities.

After defining the criteria for the MyDRTV and Toxic Chemical Industrie. We decided based on
those analysis, a technology stack for the projects. We went forward with developing the criteria,
analytical hierarchy process model and prototype for HolidayHouse. Now that we have
completed the exam project we can conclude that the HolidayHouse was the one that best fitted
our interest and the scope of the project.

Early on we decided to utilize the analytical hierarchy process model as our primary method for
narrowing in on relevant technology selections. This approach allowed us to contemplate and
compartmentalize different important factors for the solution’s requirements and evaluate them
accordingly. The AHP eventually produces a set of unbiased suggestions, which we heavily
leaned on moving forward, both in terms of the choices for the ideal solution in a realistic
production environment as well as our prototype.

**This selection process, defining the frontend, backend and database along with the IDE
and version control strategy has helped us tremendously with developing our prototype.
It has been a useful tool, in quickly establishing a working prototype. Moreover this
supported the collaboration in our team.**


## 5. Source list

(^1) https://cassandra.apache.org
Last visited on 2-6-20

(^2) ​https://docs.oracle.com/cd/B19306_01/server.102/b14237/initparams016.htm#REFRN
Last visited on 2-6-20

(^3) ​https://docs.oracle.com/cd/B28359_01/server.111/b28318/consist.htm#CNCPT
Last visited on 2-6-20

(^4) ​https://blog.angular.io/stable-angularjs-and-long-term-support-7e077635ee9c
Last visited on 2-6-20

(^5) ​https://developer.mozilla.org/en-US/docs/Web/javascript
Last visited on 3-6-20

(^6) https://docs.google.com/document/d/1b40g-hgeJC_VEUL0Qu-FlhrTuBEU8-TqtMC-M5d3IIs/edit?usp=sha
ring
Last visited on 2-6-20

(^7) https://docs.mongodb.com/manual/replication/
Last visited on 2-6-20

(^8) Common Vulnerabilities and Exposures is a trademark of the The Mitre Corporation and sponsored by
the U.S. Department of Homeland Security (DHS).

(^9) https://www.bleepingcomputer.com/news/security/somebody-tried-to-hide-a-backdoor-in-a-popular-javasc
ript-npm-package/
Last visited on 2-6-20

(^10) https://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/
Last visited on 2-6-20

(^11) https://www.bleepingcomputer.com/news/security/52-percent-of-all-javascript-npm-packages-could-have-
been-hacked-via-weak-credentials/
Last visited on 2-6-20

(^12) https://www.cvedetails.com/product/128/PHP-PHP.html?vendor_id=
Last visited on 2-6-20

(^13) https://pecl.php.net/account-request.php
Last visited on 2-6-20

(^14) https://www.cvedetails.com/product/18211/Djangoproject-Django.html?vendor_id=
Last visited on 2-6-20

(^15) https://www.zdnet.com/article/twelve-malicious-python-libraries-found-and-removed-from-pypi/
Last visited on 2-6-20

(^16) https://www.zdnet.com/article/malicious-python-libraries-targeting-linux-servers-removed-from-pypi/
Last visited on 2-6-20

(^17) https://gist.github.com/ph00lt0/dff8714e09a5b373890428803c491648
Last visited on 2-6-20

(^18) https://www.figma.com/proto/IAJ8hJqPccMgs4Tg2E1Ruo/holiday-house?node-id=37%3A2&scaling=scal
e-down
Last visited on 2-6-20

(^19)
https://stackoverflow.com/questions/57076343/django-how-to-define-a-mysql-char-data-type-in-models/5
7076707
Last visited on 2-6-20
