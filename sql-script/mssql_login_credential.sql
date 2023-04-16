USE [master]
GO
CREATE LOGIN [etl_aw] WITH PASSWORD=N'demopass', DEFAULT_DATABASE=[AdventureWorksDW2019], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [AdventureWorksDW2019]
GO
CREATE USER [etl_aw] FOR LOGIN [etl_aw]
GO
USE [AdventureWorksDW2019]
GO
ALTER ROLE [db_datareader] ADD MEMBER [etl_aw]
GO
use [master]
GO
GRANT CONNECT SQL TO [etl_aw]
GO