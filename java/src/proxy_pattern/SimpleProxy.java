package proxy_pattern;

public class SimpleProxy extends DatabaseProxy {

  /**
   * Constructs a DatabaseService which is a proxy for `to_proxy`.
   *
   * @param to_proxy
   */
  public SimpleProxy(DatabaseService to_proxy) {
    super(to_proxy);
  }

  /**
   * A vague method for finding a certain row in the database
   *
   * @param id a unique ID to search for
   * @return a query-able identifier for the entry
   */
  @Override
  public int findEntry(int id) {
    System.out.println("Doing some upfront checking with a proxy before passing request to the "
        + "database.");
    int found_entry = this.proxied_service.findEntry(id);

    System.out.println("Proxied database found a row. Returning value...");
    return found_entry;
  }
}
