# autoplay
automatic playlist creation with last.fm data


### Data:
- LastFM data : complete timeseries history
- Association Networks : listening to songs within time bins
- Layered structure of nested classifications : bigass nosql using itertools?
- What makes users good candidate for training a model
- Good stratified sampling on obvious bias
- structure is huuuuuuge json / nosql
### Features:
- Genre Tags
- classify listening sessions by our arbitrary bins described above
- similarity scorings between two users (maybe many types?)
### Metrics:
- overlap between two users --> k means?
- check to see if they have listened to any new music
- song discovery --> how many new songs do they see in some rolling window
- retention score for songs + artists + albums
- frequency score for songs + artists + albums
- playlist as a subset of a mood


### App Features:
- proportion of new songs in given playlist, give n songs, makes a playlist --> can work on itself too
