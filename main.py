import sentry_sdk
sentry_sdk.init(
    dsn="https://a8af38d33d654a55ace4e9f26150111b@o4505204820606976.ingest.sentry.io/4505204846231552",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
result = int(2) + 'test'