### https://assist.org/api/AcademicYears
[
	{
		"Id": 74,
		"FallYear": 2023
	},
	{
		"Id": 73,
		"FallYear": 2022
	},
]


### https://assist.org/api/appsettings
{
	"maxAcademicFallYear": 2021,
	"minAcademicFallYear": 1985,
	"defaultAcademicFallYear": 2021,
	"appVersion": "assistng-public v1.34.18.0"
}

### https://assist.org/api/institutions
[
	{
		"id": 1,
		"names": [
			{
				"name": "California Maritime Academy",
				"hideInList": false
			},
			{
				"name": "California State University, Maritime Academy",
				"fromYear": 2015,
				"hideInList": false
			}
		],
		"code": "CSUMA   ",
		"prefers2016LegacyReport": false,
		"isCommunityCollege": false,
		"category": 0
	},
	{
		"id": 2,
		"names": [
			{
				"name": "Evergreen Valley College",
				"hideInList": false
			}
		],
		"code": "EVERGRN ",
		"prefers2016LegacyReport": false,
		"isCommunityCollege": true,
		"category": 2
	},
]

### https://assist.org/api/institutions/113/agreements
https://assist.org/api/institutions/<institution id>/agreements

### https://assist.org/api/agreements?receivingInstitutionId=117&sendingInstitutionId=113&academicYearId=71&categoryCode=major
https://assist.org/api/agreements?receivingInstitutionId=117&sendingInstitutionId=<institution id>&academicYearId=<academic year id>&categoryCode=<major / dept / prefix>

### https://assist.org/api/agreements/categories?receivingInstitutionId=117&sendingInstitutionId=113&academicYearId=71
https://assist.org/api/agreements/categories?receivingInstitutionId=<institution id>&sendingInstitutionId=<institution id>&academicYearId=<academic year id>

### https://assist.org/api/artifacts/24779070
https://assist.org/api/artifacts/<agreement key>

### https://assist.org/api/institutions/121/transferability/availableAcademicYears
https://assist.org/api/institutions/<institution id>/transferability/availableAcademicYears

### https://assist.org/api/transferability/courses?institutionId=121&academicYearId=68&listType=CSUTC
https://assist.org/api/transferability/courses?institutionId=<institution id>&academicYearId=<academic year id>&listType=<type>

### https://assist.org/api/transferability/categories?institutionId=121&academicYearId=68&listType=CSUTC
https://assist.org/api/transferability/categories?institutionId=<institution id>&academicYearId=<academic year id>&listType=<type>