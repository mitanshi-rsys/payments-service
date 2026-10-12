# payments-service (test repo)

Tiny repo for the BugBot Cursor SDK POC.

Known bug (JIRA-123): refund amounts with more than 2 decimals, such as `10.999`,
make the refund API return 500 instead of rounding to the nearest cent.
