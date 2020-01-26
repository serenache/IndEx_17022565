/*
Write SQL queries that can be executed on the chinook.sqlite database to provide answers the following questions.
Save your SQL to this .sql file. Do not include the query results.
In PyCharm you can right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeId, FirstName, LastName, Title
FROM Employee
WHERE Title like "IT%";


--2. List the names of all Artists and the titles of their albums
SELECT a.Name, l.Title
From Artist a
        JOIN Album l on a.ArtistId = l.ArtistId;

--3. Which track(s) features the greatest number of times in playlists and how many times is it/are they included? (list Track name and the total number of appearances in playlists).
SELECT t.Name, COUNT(PT.PlaylistId)
FROM Track t
        JOIN PlaylistTrack PT on t.TrackId = PT.TrackId
GROUP BY PT.TrackId
ORDER BY COUNT(PT.PlaylistId) DESC;


--4. Provide a list of the number of tracks by each artist
SELECT a.Name, COUNT(t.TrackId)
FROM Artist a
        JOIN Album l on a.ArtistId = l.ArtistId
        JOIN Track t on l.AlbumId = t.AlbumId
GROUP BY a.Name;


--5. How much money has been invoiced for the artist Deep Purple? (For this you can create two queries, one that shows the line item from the invoices and the total amount per line, and another that sums the totals from each line)
SELECT SUM(i.Total)
FROM Invoice i
        JOIN InvoiceLine IL on i.InvoiceId = IL.InvoiceId
        JOIN Track t on IL.TrackId = t.TrackId
        JOIN Album l on t.AlbumId = l.AlbumId
        JOIN Artist a on l.ArtistId = a.ArtistId
WHERE a.Name = "Deep Purple"

