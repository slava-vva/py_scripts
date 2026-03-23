
IF OBJECT_ID('dbo.MyTable', 'U') IS NOT NULL
BEGIN
    PRINT 'Table exists';
END
ELSE
BEGIN
    PRINT 'Table does NOT exist';
END


IF OBJECT_ID('dbo.MyProcedure', 'P') IS NOT NULL
BEGIN
    PRINT 'Procedure exists';
END


IF OBJECT_ID('dbo.MyView', 'V') IS NOT NULL
BEGIN                     
    PRINT 'View exists';
END

IF OBJECT_ID('dbo.MyFunction', 'FN') IS NOT NULL
BEGIN
    PRINT 'Function exists';
END

IF EXISTS (SELECT 1 FROM sys.objects
           WHERE object_id = OBJECT_ID('dbo.MyTable')
             AND type = 'U')
BEGIN
    PRINT 'Table exists';
END
