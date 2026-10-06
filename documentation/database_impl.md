# Database implementation

## File format

Regular text file. UTF-8 should be good since it should just be recording numbers.

## Data types

Each punch should record the time at least down to the minute. Might be nice to do down to the second to avoid most user input errors and for accurate tracking, but I assume most results would be rounded off anyways. Will there be non-punch data recorded? 
Yes, jira hours and the like.
The jira hours could be an extensible feature or stored in a different file, but then there would need to be a link between the two.
Jira hours aren't associated with a single punch, but rather a single day. I think this is a point in the column of json/day-aggregated data.

## Format

Ideas:
- json (parsable, classic)
- long list (simple, could be tmw to parse, would need to parse the whole thing to build a report)
- KV database? keys would be days, and values json objects? decent idea, but might be TMW (i.e. a relational DB would be good too but is tmw - maybe SQLLite?)
- can do a crude KV with the file and json: treat the whole file as a json obj, each obj has a day, jira hours, all the punches, etc.

## final format
{
{
    "day": "DATE",
    "punches": [time1, time2, time3 ...],
    "jira_hours": num
},
another_day
}