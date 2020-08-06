select A.FirstName as FirstName, A.LastName as LastName, B.City as City, B.State as State  from Person A  left join Address B on A.PersonId = B.PersonId
