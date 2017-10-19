This project is created in HackLikeAGirl-Hackathon for the challenge of the Lufthansa Systems. The goal was digitalize the flight management that is done on paper. This definitely isn't fun, I wanted to bring a solution to that.
In this project, you find the backend server for the reading an excel file and then transforming this to the json format.
The reasen why not an API, but an excel file is read, because a functioning API was not provided. For each flight object that is returned from the server, looks like that following:
```
{
	"situation": "normal",  
	"flight": {
		"flight_number": 1750,
		"day_of_origin": "14.10.17",
		"dep_ap_schedule": "OSL",
		"dep_day": "14.10.17",
		"dep_time": 0700,
		"arr_ap_schedule": "BCN",
		"arr_day": "14.10.17",
		"arr_time": 1020,
		"arr_day_schedule": "14.10.17",
		"ac_schedule": "BBxxx"
	}
}
```

Since there is already a properly working backend server, I want to extend/reshape the project a little bit and make avaliable and also useful!
