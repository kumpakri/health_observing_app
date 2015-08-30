Health observing app
---------------------

The user reports 4 categories of its actions/states.
1. food 	(food) 	What it eats
2. medication 	(med)	What medications it took
3. exercise	(ex)	What physical activity it had
4. conditions	(con)	How it feels, what health problems it noted, mood, etc.

User inputs those reports at home-page. <domain>/
User can access view of reports of certain category <cat> at <domain>/<cat>/
the <cat> is string listed in parenthesis above.

The default number of showed days is 30.
User can change that by typing a desired number of days <num> in path:
<domain>/<cat>/<num>/

User can view only reports with desired value <val> in certain category <cat>
at <domain>/<cat>/<val>/
understand the "desired value" as "value with substring <val>"
and change number of days <num> the same way:
<domain>/<cat>/<val>/<num>/

User can access editing page at
<domain>/edit/

User can only acces the app with admin account.
User log in user account at <domain>/admin/.
User navigates through app mostly by changing address in browser.