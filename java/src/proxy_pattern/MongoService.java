package proxy_pattern;

public class MongoService implements DatabaseService {

  /**
   * Constructs a new object.
   */
  public MongoService() {
    super();
  }

  /**
   * A dummy method to appear like a read operation on a MongoDB collection
   *
   * @param id a unique ID to search for
   * @return 1, always (dummy value)
   */
  @Override
  public int findEntry(int id) {
    System.out.println(String.format("Searching for %s in a Mongo Database", id));

    return 1;
  }
}
