logger.info("Checking newly registered domains...")
logger.info("Results:")
domains = []
for line in f:
    # Calculate the Levenshtein distance for the newly registered domains.
    new_domain = line.strip().decode('utf-8')
    logger.debug(f'Checking Levenshtein distance for {new_domain}:{DOMAIN}')
    distance = Levenshtein.distance(new_domain, DOMAIN)
    if distance <= int(LD):
        logger.info("\t(!!) {} = Distance({})\n".format(new_domain, distance))
        domains.append(new_domain)

if not domains:
    logger.info("\tNone found.")
