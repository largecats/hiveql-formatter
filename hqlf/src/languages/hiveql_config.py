# -*- coding: utf-8 -*-
# https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL
class Keywords:
    RESERVED_KEYWORDS = [
        'ALL',
        'ALTER',
        'AND',
        'ARRAY',
        'AS',
        'AUTHORIZATION',
        'BETWEEN',
        'BIGINT',
        'BINARY',
        'BOOLEAN',
        'BOTH',
        'BY',
        'CACHE',
        'CASE',
        'CAST',
        'CHAR',
        'COLUMN',
        'COMMIT',
        'CONF',
        'CONSTRAINT',
        'CREATE',
        'CROSS',
        'CUBE',
        'CURRENT',
        'CURRENT_DATE',
        'CURRENT_TIMESTAMP',
        'CURSOR',
        'DATABASE',
        'DATE',
        'DAYOFWEEK',
        'DECIMAL',
        'DELETE',
        'DESCRIBE',
        'DISTINCT',
        'DOUBLE',
        'DROP',
        'ELSE',
        'END',
        'EXCHANGE',
        'EXISTS',
        'EXTENDED',
        'EXTERNAL',
        'EXTRACT',
        'FALSE',
        'FETCH',
        'FLOAT',
        'FLOOR',
        'FOLLOWING',
        'FOR',
        'FOREIGN',
        'FROM',
        'FULL',
        'FUNCTION',
        'GRANT',
        'GROUP',
        'GROUPING',
        'HAVING',
        'IF',
        'IMPORT',
        'IN',
        'INNER',
        'INSERT',
        'INT',
        'INTEGER',
        'INTERSECT',
        'INTERVAL',
        'INTO',
        'IS',
        'JOIN',
        'LATERAL',
        'LEFT',
        'LESS',
        'LIKE',
        'LOCAL',
        'MACRO',
        'MAP',
        'MORE',
        'NONE',
        'NOT',
        'NULL',
        'NUMERIC',
        'OF',
        'ON',
        'ONLY',
        'OR',
        'ORDER',
        'OUT',
        'OUTER',
        'OVER',
        'PARTIALSCAN',
        'PARTITION',
        'PERCENT',
        'PRECEDING',
        'PRECISION',
        'PRESERVE',
        'PRIMARY',
        'PROCEDURE',
        'RANGE',
        'READS',
        'REDUCE',
        'REFERENCES',
        # 'REGEXP',
        'REVOKE',
        'RIGHT',
        # 'RLIKE',
        'ROLLBACK',
        'ROLLUP',
        'ROW',
        'ROWS',
        'SELECT',
        'SET',
        'SMALLINT',
        'START',
        'SYNC',
        'TABLE',
        'TABLESAMPLE',
        'THEN',
        'TIME',
        'TIMESTAMP',
        'TO',
        'TRANSFORM',
        'TRIGGER',
        'TRUE',
        'TRUNCATE',
        'UNBOUNDED',
        'UNION',
        'UNIQUEJOIN',
        'UPDATE',
        'USER',
        'USING',
        'UTC_TMESTAMP',
        'VALUES',
        'VARCHAR',
        'VIEWS',
        'WHEN',
        'WHERE',
        'WINDOW',
        'WITH'
    ]

    NON_RESERVED_KEYWORDS = [
        'ADD',
        'ABORT',
        'ADMIN',
        'AFTER',
        'ANALYZE',
        'ARCHIVE',
        'ASC',
        'AUTOCOMMIT',
        'BEFORE',
        'BUCKET',
        'BUCKETS',
        'CASCADE',
        'CHANGE',
        'CLUSTER',
        'CLUSTERED',
        'CLUSTERSTATUS',
        'COLLECTION',
        'COLUMNS',
        'COMMENT',
        'COMPACT',
        'COMPACTIONS',
        'COMPUTE',
        'CONCATENATE',
        'CONTINUE',
        'DATA',
        'DATABASES',
        'DATETIME',
        'DAY',
        'DAYS',
        'DBPROPERTIES',
        'DEFERRED',
        'DEFINED',
        'DELIMITED',
        'DEPENDENCY',
        'DESC',
        'DETAIL',
        'DIRECTORIES',
        'DIRECTORY',
        'DISABLE',
        'DISTRIBUTE',
        'DOW',
        'ELEM_TYPE',
        'ENABLE',
        'ESCAPED',
        'EXCLUSIVE',
        'EXPLAIN',
        'EXPORT',
        'EXPRESSION',
        'FIELDS',
        'FILE',
        'FILEFORMAT',
        'FIRST',
        'FORMAT',
        'FORMATTED',
        'FUNCTIONS',
        'HOLD_DDLTIME',
        'HOUR',
        'HOURS',
        'IDXPROPERTIES',
        'IGNORE',
        'INDEX',
        'INDEXES',
        'INPATH',
        'INPUTDRIVER',
        'INPUTFORMAT',
        'ISOLATION',
        'ITEMS',
        'JAR',
        'KEY',
        'KEYS',
        'KEY_TYPE',
        'LAST',
        'LEVEL',
        'LIMIT',
        'LINES',
        'LOAD',
        'LOCATION',
        'LOCK',
        'LOCKS',
        'LOGICAL',
        'LONG',
        'MAPJOIN',
        'MATERIALIZED',
        'METADATA',
        'MINUS',
        'MINUTE',
        'MINUTES',
        'MONTH',
        'MONTHS',
        'MSCK',
        'NORELY',
        'NOSCAN',
        'NOVALIDATE',
        'NO_DROP',
        'NULLS',
        'OFFLINE',
        'OFFSET',
        'OPERATOR',
        'OPTION',
        'OUTPUTDRIVER',
        'OUTPUTFORMAT',
        'OVERWRITE',
        'OWNER',
        'PARTITIONED',
        'PARTITIONS',
        'PLUS',
        'PRETTY',
        'PRINCIPALS',
        'PROTECTION',
        'PURGE',
        'QUARTER',
        'READ',
        'READONLY',
        'REBUILD',
        'RECORDREADER',
        'RECORDWRITER',
        'REGEXP',
        'RELOAD',
        'RELY',
        'RENAME',
        'REPAIR',
        'REPLACE',
        'REPLICATION',
        'RESTRICT',
        'REWRITE',
        'RLIKE',
        'ROLE',
        'ROLES',
        'SCHEMA',
        'SCHEMAS',
        'SECOND',
        'SECONDS',
        'SEMI',
        'SERDE',
        'SERDEPROPERTIES',
        'SERVER',
        'SETS',
        'SHARED',
        'SHOW',
        'SHOW_DATABASE',
        'SKEWED',
        'SNAPSHOT',
        'SORT',
        'SORTED',
        'SSL',
        'STATISTICS',
        'STORED',
        'STREAMTABLE',
        'STRING',
        'STRUCT',
        'SUMMARY',
        'TABLES',
        'TBLPROPERTIES',
        'TEMPORARY',
        'TERMINATED',
        'TIMESTAMPTZ',
        'TINYINT',
        'TOUCH',
        'TRANSACTION',
        'TRANSACTIONS',
        'UNARCHIVE',
        'UNDO',
        'UNIONTYPE',
        'UNLOCK',
        'UNSET',
        'UNSIGNED',
        'URI',
        'USE',
        'UTC',
        'UTCTIMESTAMP',
        'VALIDATE',
        'VALUE_TYPE',
        'VECTORIZATION',
        'VIEW',
        'WEEK',
        'WEEKS',
        'WHILE',
        'WORK',
        'WRITE',
        'YEAR',
        'YEARS',
        'ZONE'
    ]

    TOP_LEVEL_KEYWORDS = [
        'ADD',
        'AFTER',
        'ALTER COLUMN',
        'ALTER TABLE',
        'DELETE FROM',
        'EXCEPT',
        'FETCH FIRST',
        'FROM',
        'GROUP BY',
        'GO',
        'HAVING',
        'INSERT INTO',
        'INSERT',
        'LIMIT',
        'MODIFY',
        'ORDER BY',
        'SELECT',
        'SET CURRENT SCHEMA',
        'SET SCHEMA',
        'SET',
        'UPDATE',
        'VALUES',
        'WHERE'
    ]

    TOP_LEVEL_KEYWORDS_NO_INDENT = [
        'INTERSECT',
        'INTERSECT ALL',
        'MINUS',
        'UNION',
        'UNION ALL'
    ]

    NEWLINE_KEYWORDS = [
        'AND',
        'CROSS JOIN',
        'ELSE',
        'INNER JOIN',
        'JOIN',
        'LEFT JOIN',
        'LEFT OUTER JOIN',
        'OR',
        'OUTER JOIN',
        'RIGHT JOIN',
        'RIGHT OUTER JOIN',
        'THEN',
        'WHEN',
        'XOR'
    ]


# https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-MathematicalFunctions
class Functions:
    MATHEMATICAL_FUNCTIONS = [
        'round',
        'ceil',
        'ceiling',
        'rand',
        'exp',
        'ln',
        'log10',
        'log2',
        'log',
        'pow',
        'power',
        'sqrt',
        'bin',
        'hex',
        'unhdex',
        'conv',
        'abs',
        'pmod',
        'sin',
        'asin',
        'cos',
        'acos',
        'tan',
        'atan',
        'degrees',
        'radians',
        'positive',
        'negative',
        'sign',
        'e',
        'pi',
        'factorial',
        'cbrt',
        'shiftleft',
        'shiftright',
        'shiftrightunsigned',
        'greatest',
        'least',
        'width_bucket'
    ]

    COLLECTION_FUNCTIONS = [
        'size',
        'map_keys',
        'map_values',
        'array_contains',
        'sort_array'
    ]

    TYPE_CONVERSION_FUNCTIONS = ['binary', 'cast']

    DATE_FUNCTIONS = [
        'from_unixtime',
        'unix_timestamp',
        'to_date',
        'year',
        'quarter',
        'month',
        'day',
        'hour',
        'minute',
        'second',
        'weekofyear',
        'extract',
        'datediff',
        'date_add',
        'date_sub',
        'from_utc_timestamp',
        'to_utc_timestamp',
        'current_date',
        'current_timestamp',
        'add_months',
        'last_day',
        'next_day',
        'trunc',
        'months_between',
        'date_format'
    ]

    CONDITIONAL_FUNCTIONS = [
        'if',
        'isnull',
        'isnotnull',
        'nvl',
        'COALESCE',
        'nullif',
        'assert_true'
    ]

    STRING_FUNCTIONS = [
        'ascii',
        'base64',
        'character_length',
        'chr',
        'concat',
        'context_ngrams',
        'concat_ws',
        'decode',
        'elt',
        'encode',
        'field',
        'find_in_set',
        'format_number',
        'get_json_object',
        'in_file',
        'instr',
        'length',
        'locate',
        'lower',
        'lpad',
        'ltrim',
        'ngrams',
        'octet_length',
        'parse_url',
        'printf',
        'quote',
        'regexp_extract',
        'regexp_replace',
        'repeat',
        'replace',
        'reverse',
        'rpad',
        'rtrim',
        'sentences',
        'space',
        'split',
        'str_to_map',
        'substr',
        'substring_index',
        'translate',
        'trim',
        'unbase64',
        'upper',
        'initcap',
        'levenhtein',
        'soundex'
    ]

    DATA_MASKING_FUNCTIONS = [
        'mask',
        'mask_first_n',
        'mask_last_n',
        'mask_show_first_n',
        'mask_show_last_n',
        'mask_hash'
    ]

    MISC_FUNCTIONS = [
        'java_method',
        'reflect',
        'hash',
        'current_user',
        'logged_in_user',
        'current_database',
        'md5',
        'sha1',
        'sha',
        'crc32',
        'sha2',
        'aes_decrypt',
        'version',
        'surrogate_key'
    ]

    AGGREGATE_FUNCTIONS = [
        'count',
        'sum',
        'avg',
        'min',
        'max',
        'variance',
        'var_samp',
        'stddev_pop',
        'stddev_samp',
        'covar_pop',
        'covar_samp',
        'corr',
        'percentile',
        'percentile_approx',
        'regr_avgx',
        'regr_avgy',
        'regr_count',
        'regr_intercept',
        'regr_r2',
        'regr_slope',
        'regr_sxx',
        'regr_sxy',
        'regr_syy',
        'histogram_numeric',
        'collect_set',
        'collect_list',
        'ntile'
    ]

    TABLE_GENERATING_FUNCTIONS = [
        'explode',
        'posexplode',
        'inline',
        'stack',
        'json_tuple',
        'parse_url_tuple'
    ]

    # https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics#LanguageManualWindowingAndAnalytics-EnhancementstoHiveQL
    WINDOWING_FUNCTIONS = ['LEAD', 'LAG', 'FIRST_VALUE', 'LAST_VALUE']

    ANALYTICS_FUNCTIONS = [
        'RANK',
        'ROW_NUMBER',
        'DENSE_RANK',
        'CUME_DIST',
        'PERCENT_RANK',
        'NTILE'
    ]