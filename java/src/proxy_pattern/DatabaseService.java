package proxy_pattern;

/**
 * Unifies a set of methods for CRUD operations with different database systems.
 *
 * @author Jesse Steinberg
 */
public interface DatabaseService {

  /**
   * A vague method for finding a certain row in the database
   *
   * @param id a unique ID to search for
   * @return a query-able identifier for the entry
   */
  public int findEntry(int id);
}
