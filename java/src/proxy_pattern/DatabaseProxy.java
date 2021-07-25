package proxy_pattern;

/**
 * An implementation of `DatabaseService` which contains another DatabaseService.
 *
 * Does not implement any business logic directly, simply functions as an intermediary between
 * users and direct database operations.
 */
public abstract class DatabaseProxy implements DatabaseService {
  protected DatabaseService proxied_service;

  /**
   * Constructs a DatabaseService which is a proxy for `to_proxy`.
   */
  public DatabaseProxy(DatabaseService to_proxy) {
    super();
    this.proxied_service = to_proxy;
  }
}
